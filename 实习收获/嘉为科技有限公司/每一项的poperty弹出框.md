```js
                <bk-table-column label="操作" width="160" v-if="permissionData.start_vm_put === 'PUT' ||
                    permissionData.stop_vm_put === 'PUT' || permissionData.restart_vm_put === 'PUT'">
                    <template slot-scope="props">
                        <bk-button v-if="permissionData.start_vm_put === 'PUT'" text :disabled="props.row.status !== 'STOP'"
                            @click="operateItem([props.row], 'turnOn')">开机</bk-button>
                        <bk-button v-if="permissionData.stop_vm_put === 'PUT'" text :disabled="props.row.status !== 'RUNNING'"
                            @click="operateItem([props.row], 'turnOff')">关机</bk-button>
                        <bk-popover class="dot-menu" placement="bottom-start" theme="dot-menu light" trigger="click" :arrow="false"
                            offset="15" :distance="0">
                            <div class="btn-layout"><bk-button text>更多</bk-button><bk-icon type="down-shape" class="more" /></div>
                            <ul class="dot-menu-list" slot="content">
                                <li>
                                    <bk-button text v-if="permissionData.restart_vm_put === 'PUT'" size="small"
                                        @click="operateItem([props.row], 'restart')" :disabled="props.row.status !== 'RUNNING'">重启</bk-button>
                                </li>
                                <li>
                                    <bk-button text @click="showChange(props.row)" size="small">标签</bk-button>
                                </li>
                                <li>
								<li>
                                    <bk-button v-if="permissionData.reset_password_put === 'PUT' && props.row.cloud_type !== 'openstack'" text
                                        @click="operateItem([props.row], 'resetpassword')" size="small"> 重置密码</bk-button>
                                </li>
```
这里更多使用ul 和 li实现的
利用template slot-scope获取每一行的数据
每一项一个button 绑定一个click


```js
// 操作按钮
operateItem(data, operate, batch) {
	if (operate === 'resetpassword') {
		this.isResetPsw = true
		this.resetPswFormData.resource_id = data[0].resource_id
		this.resetPswFormData.resource_name = data[0].resource_name
		this.resetPswFormData.account_id = data[0].account_id
		return
	}
```
click绑定


```js
<bk-dialog class="form-modal" v-model="isResetPsw" title="重置密码" width="640">
	<bk-form :label-width="100" ref="resetPswForm"
		v-bkloading="{ isLoading: resetPswLoading, zIndex: 10 }"
		:model="resetPswFormData" :rules="resetPswFormRules">
		<bk-form-item label="用户名：">
			<div>root (Linux) / administrator (Windows)</div>
		</bk-form-item>
		<bk-form-item label="新密码：" property="newPsw">
			<bk-input v-model="resetPswFormData.newPsw" type="password" />
		</bk-form-item>
		<bk-form-item label="确认密码：" property="confirmPsw">
			<bk-input v-model="resetPswFormData.confirmPsw" type="password" />
		</bk-form-item>
		<bk-form-item>
			<div>您所选的<bk-button :text="true" @click="showInstance = !showInstance">实例</bk-button>将执行重置密码操作，您是否确定操作</div>
			<div class="instance" v-show="showInstance">{{vmInfo.resource_id}} / {{vmInfo.resource_name}}</div>
		</bk-form-item>
		<bk-form-item>
			<bk-alert type="warning" title="修改密码后需要重启实例生效。"></bk-alert>
		</bk-form-item>
	</bk-form>
	<div slot="footer">
		<bk-button @click="resetPsw" :loading="resetPswLoading">重置</bk-button>
		<bk-button @click="isResetPsw = false">取消</bk-button>
	</div>
</bk-dialog>
```

然后一个dialog



```js
resetPswFormData: {
	newPsw: '',
	confirmPsw: '',
	resource_id: '',
	resource_name: '',
	account_id: ''
}
```

一个formdata

```js
showResetPsw() {
	this.showInstance = false
	this.isResetPsw = true
	this.resetPswFormData = {
		newPsw: '',
		confirmPsw: ''
	}
},
```

click之后


密码的判断
```js
            
        created() {
this.resetPswFormRules = {
	newPsw: [
		{
			required: true, message: '请输入新密码', trigger: 'blur change'
		}, {
			validator: this.checkNewPsw, message: '密码长度8-20位，必须包含英文字母+数字+特殊字符', trigger: 'blur change'
		}
	],
	confirmPsw: [
		{
			required: true, message: '请输入确认密码', trigger: 'blur change'
		}, {
			validator: this.checkConfirmPsw, message: '两次输入密码不一致!', trigger: 'blur change'
		}
	]
}
```



```js

// 密码校验
checkNewPsw(val) {
	return val.match(/(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9]).{8,20}/)
},
checkConfirmPsw(val) {
	return val === this.resetPswFormData.newPsw
}
```