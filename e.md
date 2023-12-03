excel
table封装
组件通讯
组件拆分


```jsx
export default (props) => {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState([]);
  const { pageName, getApi } = props;
  const { location: { pathname } } = window;
  const path = pathname.split('/')[3];

  const columns = [
    {
      title: '评价功能',
      dataIndex: 'name',
      width: '20%',
      render: (name, record) => <span>{path === 'holisticScore' ? name : <a href={`${ROUTEBASE}/devevaluate/detail?id=${record.id}&path=${path}`}>{name}</a>}</span>,
    },
    {
      title: '评价时间',
      dataIndex: 'time',
    },
    {
      title: '评价人数',
      dataIndex: 'evaluationNumber',
    },
    {
      title: '平均分',
      dataIndex: 'averageScore',
    },
    {
      title: '科学得分',
      dataIndex: 'scientificScore',
    },
  ];
  const fields = (dataitem) => {
    console.log(dataitem);
    { id: 1, name: '111'}
    const fields = [];
    const obj = {};
    for (let i = 0, { length } = columns; i < length; i++) {
      fields.push(columns[i].title);
      if (dataitem) obj[columns[i].title] = dataitem[columns[i].dataIndex];
    }
    return { fields, obj };
    // fields存放title名字 fields = [科学得分]
    // obj存放对应的数据字段 obj = ['科学得分'-> scientificScore]
  };

  const getTableDatas = (rangeDate) => {
    setLoading(true);
    getApi({ startTime: rangeDate[0].valueOf(), endTime: rangeDate[1].valueOf() }, (datas) => {
      if (datas) {
        for (let j = 0, len = datas.length; j < len; j++) {
          const time = rangeDate;
          datas[j].time = `${moment(time[0]).format(dateFormat)}-${moment(time[1]).format(dateFormat)}`;
        }
        setData(datas);
      }
    }).finally(() => setLoading(false));
  };

  useEffect(() => {
    getTableDatas(defaultValue);
  }, []);

  const exportExcel = (callback, rangeDate) => {
    getApi({ startTime: rangeDate[0].valueOf(), endTime: rangeDate[1].valueOf() }, (datas) => {
      if (datas) {
        for (let j = 0, len = datas.length; j < len; j++) {
          const time = rangeDate;
          datas[j].time = `${moment(time[0]).format(dateFormat)}-${moment(time[1]).format(dateFormat)}`;
        }
        const dataTable = []; // excel文件中的数据内容
        if (data && data.length > 0) {
          for (const i in data) { // 循环获取excel中每一行的数据
            dataTable.push(fields(data[i]).obj); // 设置excel中每列所获取的数据源
          }
        }
        const options = {
          fileName: pageName,
          datas: [
            {
              // 父组件传递的要导出的数据
              sheetData: dataTable,
              // sheet名字
              sheetName: 'sheet',
              // 父组件传递过来的要导出的数据的key值是一个数组
              sheetFilter: fields().fields,
              // Excel表格的表头,在父组件中传递的时候注意与key对应
              sheetHeader: fields().fields,
            },
          ],
        };
        callback(options);
      }
    });
  };
```

![[e.png]]
dataTable