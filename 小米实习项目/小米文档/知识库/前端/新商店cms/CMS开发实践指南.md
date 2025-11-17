待补充：使用场景 & 代码解析 & 整体流程

技术库：react

hooks库：[ahooks](https://ahooks.js.org/zh-CN/hooks/use-request/index)

UI库：[antd5](https://ant.design/components/overview-cn)

1. # 新建路由
    

路由配置文件：src/routers/config/index.js

路由组件：src/routers/Routes.js

```JavaScript
          {
            path: '/content/warehouse',
            name: '内容仓库',
            menu: true,
            routes: [
              {
                path: '/content/warehouse/pool-list',
                name: '内容卡片',
                menu: true,
                component: lazy(() =>
                  import('src/views/Content/ContentWarehouse/Pool/List.tsx')
                ),
                meta: {
                  auth: true,
                },
              },
              {
                path: '/content/warehouse/pool-new',
                name: '新建内容卡片',
                menu: false,
                statusKey: 'contentPoolStatus',
                nameMap: {
                  show: '查看内容卡片',
                  edit: '编辑内容卡片',
                  add: '新建内容卡片',
                  breadNav: '内容卡片',
                },
                component: lazy(() =>
                  import(
                    'src/views/Content/ContentWarehouse/Pool/NewOrEdit.tsx'
                  )
                ),
              },
            ],
          },
```

- path：地址栏显示路径
- name：菜单上显示名字
- menu：是否在菜单上显示
- component：菜单页对应加载的组件
- meta
    - auth：是否有权限验证（具体见`src/views/App/App.js`）
- routes：子项路由配置数组
- statusKey：指定当前详情页状态的字段
- nameMap：对应不同状态时，详情页展示的标题

为什么对于详情页需要设置statusKey和nameMap?

- `src/views/App/components/RouteHeader.tsx`
    

2. # 首页
    

页面模板：src/views/pageModel/components/Model.tsx

```TypeScript
type ModelProps = {
  tableQuery?: (params: any) => Promise<NetWorkResponse>; // 表格请求
  tableConfig?: TableProps<any> & {
    getColumns?: (params: Record<string, any>) => ColumnsType<any>;
  }; // 表格props配置
  queryConfig?: SelectionFormProps; // 搜索区域配置
  operationList?: Array<buttonConfigProps>; // 表格外操作按钮配置 -- 对象形式配置
  getOperationList?: (params: Record<string, any>) => Array<buttonConfigProps>; // 表格外操作按钮配置 -- 函数形式配置
};
```

```TypeScript
<PageModel
      className='section-style-16'
      queryConfig={{ formItems: formItemsConfig({ filterGroup }) }}
      getOperationList={({ query }) => getOperationList(selectedRows, query)}
      tableConfig={{
        getColumns: ({ query }) => getColumnsConfig({ filterGroup, query }),
        rowKey: 'contentId',
        rowSelection: {
          type: 'checkbox',
          onChange: onSelectedChange,
        },
      }}
      tableQuery={request}
    />
```

1. ## 搜索
    

一般只有两种搜索框，文本输入框和下拉搜索框。

1. ### 文本输入框
    

```TypeScript
{
      name: 'id',
      type: InputType.Text,
      fieldProps: {
        placeholder: 'ID',
      },
 },
```

2. ### 下拉搜索
    

1. #### 静态选项
    

```TypeScript
{
      name: 'status',
      type: SelectionType.Selection,
      fieldProps: {
        placeholder: '发布状态',
        mode: 'multiple', // 是否多选
        showArrow: true, // 是否显示后面的箭头
        options: ReleaseStatusOptions, // 选项数组[{label:xx,value:xx}]
      },
 },
```

2. #### 可配置选项
    

```TypeScript
{
      name: 'tipScene',
      type: SelectionType.Selection,
      fieldProps: {
        placeholder: '提示场景',
        mode: 'multiple',
        showArrow: true,
        options: filterGroup?.tipScene || [],
      },
  },
```

针对这种情况，封装了公共hook`useFilterGroup`_（__scr__/utilities/hooks/useFilterGroup.ts）_

```TypeScript
const { filterGroup } = useFilterGroup({
    params: {
      filterTypeList: ['contentPoolType', 'planType'],
    },
  });
```

3. #### 远程搜索
    

```TypeScript
{
      name: 'planName',
      type: SelectionType.Selection,
      fieldProps: {
        placeholder: '计划名称',
        mode: 'multiple',
        showArrow: true,
        showSearch: true, // 控制antd Select是否可搜索
        searchRequest: true, // 是否开启远程搜索
        request: (value: string) => { // 搜索请求
          if (!value) return;
          return new GetSuggestService({
            fieldType: 'planName',
            keyword: value,
          }).get({ path: 'plan' });
        },
      }
    },
```

远程搜索的接口与服务端已做约定，接口名称与参数需要按钮规范走，前端侧封装接口`GetSuggestService`

规范见下：

通用接口说明：

1、模糊搜索sug接口规范

接口路径：GET: /${model}/fields/suggest

请求参数：

|   |   |   |   |
|---|---|---|---|
|参数名|类型|是否必填|含义|
|fieldType|String|是|字段名举例：根据模块业务情况自定义<br><br>'appId' 'appName'|
|keyword|String|是|关键词|

2. ## 按钮
    

按钮组件：src/views/pageModel/components/Buttons.tsx

```TypeScript
enum buttonClickType {
  OPEN_DIALOG = 'openDialog', // 打开操作弹窗
  OPEN_INFO_DIALOG = 'openInfoDialog', // 打开简单提醒弹窗
  OPEN_DRAWER = 'openDrawer', // 打开抽屉
  JUMP_PAGE = 'jumpPage', // 跳转页面
  CUSTOM = 'custom', // 自定义
}

{
      type: 'primary' as const,
      name: '新建资源位',
      icon: <PlusOutlined />,
      clickType: buttonClickType.JUMP_PAGE,
      clickConfig: {
        path: '/content/resource-manage/resource-position-new',
        stateParams: {
          status: TaskStatus.Add,
        },
      },
  },
```

```TypeScript
{
      name: '导出数据',
      disabled: true,
      icon: <DownloadOutlined />,
      clickType: buttonClickType.CUSTOM,
      clickFn: () => {
        alert('暂不支持导出数据');
      },
  },
```

3. ## 表格
    

1. ### 自定义表格显示
    

```TypeScript
{
      title: '提示页面',
      dataIndex: 'tipPage',
      render: (data: string) =>
        filterGroup['tipPage']?.filter(
          (item: { label: string; value: string }) => item.value === data
        )?.[0]?.label,
    },
```

2. ### 状态显示
    

```TypeScript
{
      title: '发布状态',
      dataIndex: 'status',
      render: (data: number) => (
        <Space>
          <Badge color={colors[data as keyof typeof colors]} />
          {
            ReleaseStatusOptionsV2.filter(
              (item: Record<string, any>) => item.value === data
            )?.[0]?.label
          }
        </Space>
      ),
    },
```

3. ### 带排序
    

```TypeScript
{
      title: '上线时间',
      dataIndex: 'startTime',
      width: 120,
      sorter: (row1: Record<string, any>, row2: Record<string, any>) =>
        row1.startTime - row2.startTime,
      render: (data: number) => dayjs(data).format('YYYY-MM-DD HH:mm:ss'),
    },
```

4. ### 操作按钮
    

```TypeScript
{
      title: (
        <Space>
          操作
          <Tooltip title='已上线的计划无法删除/编辑，如需操作需要先下线; 已下线的计划不可编辑'>
            <QuestionCircleOutlined />
          </Tooltip>
        </Space>
      ),
      dataIndex: 'planId',
      width: 200,
      fixed: 'right',
      render: (planId: string, record: Record<string, any>) => {
        return (
          <ButtonsOperation
            operationList={[
              {
                name: '查看',
                type: 'link',
                size: 'small',
                clickType: buttonClickType.JUMP_PAGE,
                clickConfig: {
                  path: '/content/schedule/plan-management-new',
                  stateParams: {
                    planStatus: TaskStatus.Show,
                    planId,
                  },
                },
              },
            ]}
            spaceProps={{ size: 0, wrap: true }}
          />
        );
      },
    },
```

3. # 新建
    

表单项渲染：src/components/Form/formItem.tsx

```TypeScript
export type FormItemConfigProps = PickFromItemProps & {

  type?: FormItemType;  // 表单项类型

  fieldProps?: ( 
    | InputProps
    | InputNumberProps
    | SelectProps<any>
    | DatePickerProps
    | TextAreaProps
    | RangePickerProps<any>
    | GroupProps
  ) &
    SelectionProps;
  formItemProps?: FormItemProps;
  
  // 依赖配置
  dependency?: string;
  dependencyValues?: string[];
  calculateDependencies?: (getFieldValue: (name: NamePath) => any) => boolean;
  checkUpdate?: (prevValues: any, nextValues: any) => boolean; // 自定义检查是否更新展示

  // 如果formItem的某个属性值需要依赖于其他Item的值来处理，那么可以通过这个函数获取到对应的字段值，并在处理完后返回对应的props
  handleFieldProps?: (
    getValue?: (name: NamePath) => any
  ) => Record<string, any>;
  
};
```

1. ## BaseForm
    

基础的一个表单组件，预设有取消和提交两个操作按钮

主要传入FormItemConfig和自定义提交函数，即可完成一个表单的功能

```TypeScript
type BaseFormProps = {
  form: FormInstance; // 表单实例
  formItems: FormItemConfigProps[]; // 表单项配置，见上
  formProps?: FormProps; // 表单（<Form>组件）的props配置
  onCancel?: () => void;  // 取消函数
  onFinsh?: (values: any) => void; // 提交函数
  children?: RenderProps | React.ReactNode // 自定义按钮组件
};
```

```HTML
<BaseForm
        formItems={[
         {
            name: 'modelName',
            label: '机型名称',
            type: InputType.Text,
            formItemProps: {
                rules: [{ required: true }],
           },
         },
        ]}
        onFinish={onFinish}
        form={form}
        onCancel={onCancel}
   />
```

2. ## SchemaForm
    

与baseForm不同的一点，是表单项的数据来自于后台配置，优势在于可以**不更改代码更替表单项配置**

```TypeScript
 type SchemaFormProps =  {
  formConfig: CustomItemsType[]; // schema配置
  selectRequestConfig?: Record<string, any>; // 搜索函数配置
  onClose?: () => void;
  onFinsh?: (values: any) => void; 
};

<SchemaForm
        formConfig={appConfig}
        form={form}
        selectRequestConfig={{
          getAppInfo: (appId: string[]) => {
            if (!appId) return;
            return getAppInfo(appId, form);
          },
        }}
      >
```

1. 读取配置（业务处理）
    

```TypeScript
 import useQuerySchemaDetail from 'src/utilities/hooks/useQuerySchemaDetail';
 
 const { schemaConfig: appConfig } = useQuerySchemaDetail({
    contentPoolType: 'app_guide_new_app_info',
  });
```

2. 格式化config（公共处理）
    

```TypeScript
import formatSchema from 'src/utilities/common/formatSchema'

useEffect(() => {
    setFormatConfig(formatSchema(formConfig, selectRequestConfig));
}, [formConfig, selectRequestConfig]);
```

3. ## stepsForm
    

src/components/Form/stepForms/stepForms.tsx

分步表单，将表单配置分成多步骤，由步骤条和各式表单组成

```HTML
<StepsForm
        items={getStepsConfig(state.planStatus)} // 分步显示配置
        stepItemsFormConfig={config} // 分步内容配置，[step1Config,step2Config]
        initValues={formValues} // 初始表单值
        readOnly={state?.planStatus === TaskStatus.Show} // 是否为只读状态
        selectRequestConfig={{ // 筛选项请求
          contentType: () =>
            Promise.resolve({
              data: filterGroup['contentType'],
            }),
        }}
         onSubmit={(values,callback)=>{} } // 提交函数
   />
```

1. ### 分步显示配置
    

一般前面几个步骤为表单，最后一页为反馈

```JavaScript
const baseStepConfig = [
    {
      title: '集合信息',
      description: '请填写集合信息',
    },
    {
      title: '集合配置',
      description: '请填写集合配置信息',
    },
    // 根据是否提交成功，决定最后一步显示的内容
    isSubmitSuccess ? 
  {
       title: '提交成功',
       description: '屏蔽信息提交成功',
   }
  : {
        title: '提交失败',
        description: '屏蔽信息提交失败',
   },
  ];
  
  // 在查看模式下，不显示反馈步
 status === TaskStatus.Show && (stepConfig.splice(1,1))
```

2. ### 表单配置
    

1. basicForm
    

```JavaScript
{
      type: FormType.BasicForm,
      config: [
      {
        label: '分桶名称',
        name: 'bucketName',
        type: SelectionType.Selection,
        colProps: {
          span: 12,
        },
        fieldProps: {
          options: filterGroup['bucketName'],
        },
       formItemProps: {
        rules: [{ required: true }],
      },
    }],
},
```

2. schemaForm
    

```JavaScript
{
      type: FormType.SchemaForm,
      config: () => ({
        name: 'new_ad_ban_step1',
      }),
 },
```

3. Custom：需要根据当前步表单值更替下一步的表单配置
    

```JavaScript
{
      type: FormType.Custom,
      // params : 上一步表单的存储值
      config: (params: Record<string, any> = {}) => {
        const { contentType } = params;
        if (contentType === ContentType.ClientTab) {
          return {
            type: FormType.ClientTab,
          };
        } else {
          return {
            type: FormType.SchemaForm,
         }
           
      },
    },
```

4. children：当某一步的表单比较复杂，不能使用配置完成
    

```HTML

 <StepsForm
     {...其他配置}
     childrens={[
         null,
         () => (
            <TabConfigComp
              ModalFormConfig={ModalFormConfig}
              initValues={initialValues[1]}
            />
          ),
          null,
 ]}
  />
```

5. result：结果反馈页
    

```TypeScript
{
      type: FormType.Result,
      // result：请求结果
      config: (result: Record<string, any>) =>
        result?.code === 0
          ? {
              status: 'success' as ResultStatusType,
              title: '提交成功',
              subTitle: (
                <span>
                  屏蔽信息已提交成功，请前往列表页查看。
                  <br />
                  屏蔽信息关联客户端内容发布，创建完请进行充分验证，避免出现下发配置与预期不符的情况发生。
                </span>
              ),
              extra: [
                <Button key='adBanList' type='primary'>
                  <Link to={`/search/${mediaType}/ad-ban-list`}>返回列表</Link>
                </Button>,
              ],
            }
          : {
              status: 'error' as ResultStatusType,
              title: '提交失败',
              subTitle: (
                <span>
                  {result?.message}
                  <br />
                  请返回修改后重新提交。
                </span>
              ),
              extra: [
                <Button key='adBanList' type='default'>
                  <Link to={`/search/${mediaType}/ad-ban-list`}>退出</Link>
                </Button>,
                <Button key='adBanList' onClick={onBack} type='primary'>
                  上一步
                </Button>,
              ],
            },
    },
```

4. # 其他场景
    

1. ## 编辑|查看|复制（二级页面）
    

```JavaScript
{
                name: '查看',
                type: 'link',
                size: 'small',
                clickType: buttonClickType.JUMP_PAGE,
                clickConfig: {
                  path: '/content/resource-manage/tab-version-new',
                  stateParams: {
                    status: TaskStatus.Show, // show\edit\add
                    id,
                  },
                },
     },
```

编辑：比新建多了一次初始请求

查看：比编辑少了个保存按钮

复制：编辑的场景，新建的接口

2. ## 删除|发布|下线 （弹窗场景）
    

一套配置，换接口

```TypeScript
{
                name: '发布', // 按钮名称
                type: 'link',
                size: 'small',
                disabled: ReleaseStatus.NotOnline !== record.status, // 禁止点击条件
                clickType: buttonClickType.OPEN_INFO_DIALOG,
                clickConfig: {
                  title: `ID：${data}`,
                  content: '请确认是否发布该文案？',
                  onOk: (close: any) => {
                    new PushTipManageService({
                      tipId: data,
                    })
                      .post({
                        path: {
                          suffixPath: 'pushonline',
                        },
                      })
                      .then(() => {
                        notification.success({
                          message: '发布成功',
                          description: `成功发布ID为${data}的文案`,
                        });
                        query(); // 刷新列表
                      })
                      .finally(() => {
                        close();
                      });
                  },
                },
              },
```

3. ## 预览（抽屉场景）
    

一套配置，换key

```TypeScript
import previewConfig from 'src/views/Common/config/previewDrawerConfig';

{
                name: '预览',
                type: 'link',
                size: 'small',
                disabled: ReleaseStatus.Offline === record.status,
                clickType: buttonClickType.OPEN_DRAWER,
                clickConfig: previewConfig(
                previewDistributeKey.CLOUD_APP,  // 模块key，与服务端约定
                {
                  distributionScene: '云化应用名单', // 标题
                  id: data, // 需要预览的配置id
                  path: 'cloud/app/preview', // 白名单推送接口
                  idType: PreviewIdType.DID, // 白名单推送的类型，OAID\DID\
                }),
 },
```

  

5. # 问题单
    

## 问题1:xxx