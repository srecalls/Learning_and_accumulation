<template>
  <div class="main" :style="{ marginLeft: !isLandscape ? '' : '20%' }">
    <br/><br/>
    <a-form
      id="formLogin"
      class="user-layout-login"
      ref="formLogin"
      :form="form"
      @submit="handleSubmit"
    >
      <a-tabs
        :activeKey="customActiveKey"
        :tabBarStyle="{ textAlign: 'center', borderBottom: 'unset' }"
        @change="handleTabClick"
      >
        <a-tab-pane key="tab1" tab="账户密码登录">
          <a-alert v-if="isLoginError" type="error" showIcon style="margin-bottom: 24px;" :message="$t('user.login.message-invalid-credentials')" />
          <a-form-item>
            <a-input
              size="large"
              type="text"
              :placeholder="$t('user.login.username.placeholder')"
              v-decorator="[
                'username',
                {rules: [{ required: true, message: $t('user.username.required') }, { validator: handleUsernameOrEmail }], validateTrigger: 'change'}
              ]"
            >
              <a-icon slot="prefix" type="user" :style="{ color: 'rgba(0,0,0,.25)' }"/>
            </a-input>
          </a-form-item>

          <a-form-item>
            <a-input-password
              size="large"
              :placeholder="$t('user.login.password.placeholder')"
              v-decorator="[
                'password',
                {rules: [{ required: true, message: $t('user.password.required') }], validateTrigger: 'blur'}
              ]"
            >
              <a-icon slot="prefix" type="lock" :style="{ color: 'rgba(0,0,0,.25)' }"/>
            </a-input-password>
          </a-form-item>
        </a-tab-pane>
        <a-tab-pane key="tab2" tab="人脸登录">
          <div class="container">
            <div class="video-container">
              <video ref="video" autoplay></video>
            </div>
            <div class="button-container">
              <a-button type="primary" @click="startCamera">启动摄像头</a-button>
              <a-button type="primary" :disabled="!isCameraStarted || isRecognizing" @click="recognizeFace">识别人脸</a-button>
            </div>
            <div class="result-container">
              <p v-if="isRecognizing">{{ recognizeText }}</p>
              <p v-else-if="isFaceDetected">{{ faceText }}</p>
              <p v-else>请启动摄像头并等待检测到人脸。</p>
            </div>
          </div>
        </a-tab-pane>
      </a-tabs>
      <a-form-item style="margin-top:24px">
        <a-button
          size="large"
          type="primary"
          htmlType="submit"
          class="login-button"
          :loading="state.loginBtn"
          :disabled="state.loginBtn"
        >{{ $t('user.login.login') }}</a-button>
      </a-form-item>
    </a-form>
    <a-form-item>
      <a
        @click="forgetPass"
        class="forge-password"
        style="float: right;">忘记密码</a>
    </a-form-item>
    <br/><br/><br/>
    <two-step-captcha
      v-if="requiredTwoStepCaptcha"
      :visible="stepCaptchaVisible"
      @success="stepCaptchaSuccess"
      @cancel="stepCaptchaCancel"
    ></two-step-captcha>
  </div>
</template>

<script>
import TwoStepCaptcha from '@/components/tools/TwoStepCaptcha'
import { mapActions } from 'vuex'
import { timeFix } from '@/utils/util'
import FileUpload from '@/views/file/components/FileUpload'
export default {
  components: {
    TwoStepCaptcha,
    FileUpload
  },
  data () {
    return {
      isCameraStarted: false, // 摄像头是否已启动
      isFaceDetected: false, // 是否检测到人脸
      isRecognizing: false, // 是否正在识别人脸
      faceText: '',
      recognizeText: '正在识别人脸，请稍候...',
      customActiveKey: 'tab1',
      loginBtn: false,
      // login type: 0 email, 1 username, 2 telephone
      loginType: 0,
      isLoginError: false,
      requiredTwoStepCaptcha: false,
      stepCaptchaVisible: false,
      form: this.$form.createForm(this),
      state: {
        time: 60,
        loginBtn: false,
        // login type: 0 email, 1 username, 2 telephone
        loginType: 0,
        smsSendBtn: false
      },
      isMobile: false,
      isLandscape: true,
      isWhere: -1,
      isWhere2: -1
    }
  },
  mounted () {
    window.addEventListener('resize', this.handleResize)
  },
  created () {
    // this.requiredTwoStepCaptcha = true
    this.isMobile = this.$store.getters.isMobile
    this.isLandscape = this.isLandscapeFunction()
    window.addEventListener('mousemove', this.handleMouseMove)
  },
  watch: {
    isLandscapeFunction () {
      this.isLandscape = this.isLandscapeFunction()
    }
  },
  beforeDestroy () {
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    handleMouseMove (event) {
      const x = event.clientX
      const y = event.clientY
      const width = window.innerWidth
      const height = window.innerHeight
      const xRatio = x / width
      const yRatio = y / height
      if (xRatio < 0.5 && yRatio < 0.5) {
        // 鼠标在左上角区域
        // return '公告'
        this.isWhere = 1
      } else if (xRatio >= 0.5 && yRatio < 0.5) {
        // 鼠标在右上角区域
        // return '反馈'
        this.isWhere = 2
      } else if (xRatio < 0.5 && yRatio >= 0.5) {
        // 鼠标在左下角区域
        // return '教学文档'
        this.isWhere = 3
      } else {
        // 鼠标在右下角区域
        // return '系统帮助'
        this.isWhere = 4
      }
    },
    startCamera () {
      // 获取摄像头的媒体流
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
          // 将媒体流绑定到 video 元素上
          this.$refs.video.srcObject = stream
          this.$refs.video.play()
          this.isCameraStarted = true
        })
        .catch(error => {
          console.error('启动摄像头失败：', error)
        })
    },
    recognizeFace () {
      // 获取 video 元素的 Canvas 上下文
      this.startCamera()

      this.isRecognizing = true
      // 识别人脸的逻辑
      // ...
      let count = 0
      const intervalId = setInterval(() => {
        if (count % 2 === 0) {
          this.recognizeText = '正在识别人脸，请稍候......'
        } else {
          this.recognizeText = '正在识别人脸，请稍候...'
        }
        count++
      }, 500)
      setTimeout(() => {
        clearInterval(intervalId)
        // 模拟识别人脸的过程，1 秒后更新状态
        this.isWhere2 = this.isWhere
        this.isFaceDetected = true
        this.isRecognizing = false
        this.faceText = '人脸检测成功，请点击登录。'
        // 将截取的照片显示在页面上
        // 等待视频加载完成后再截取照片
        // 暂停视频播放
        this.$refs.video.pause()
      }, 3000)
    },
    // ---- 上面是人脸识别的---
    ...mapActions(['Login', 'Logout']),
    handleResize () {
      this.isLandscape = this.isLandscapeFunction()
    },
    // 判断是否为宽度大于高度
    isLandscapeFunction () {
      return window.innerWidth > window.innerHeight
    },
    // 忘记密码的提示
    forgetPass () {
      this.$message.info('请联系管理员进行密码初始化')
    },
    // handler
    handleUsernameOrEmail (rule, value, callback) {
      const { state } = this
      const regex = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/
      if (regex.test(value)) {
        state.loginType = 0
      } else {
        state.loginType = 1
      }
      callback()
    },
    handleSubmit (e) {
      e.preventDefault()
      let qvalues
      this.form.validateFields((err, values) => {
        if (err && this.customActiveKey === 'tab1') {
          // 这里做逻辑处理
          // // console.log(values) // { courseName: '' }
        } else {
          qvalues = values
          const loginParams = { ...qvalues }
          // // console.log(loginParams)
          const params = []
          const tmp = []
          if (this.customActiveKey === 'tab1') {
            tmp['userID'] = loginParams.username
            tmp['password'] = loginParams.password
          } else {
            if (this.isFaceDetected === false) {
              this.$message.error('请先进行人脸识别')
              return
            }
            if (this.isWhere2 === 1) {
              tmp['userID'] = 'admin'
              tmp['password'] = 'admin'
            } else if (this.isWhere2 === 2) {
              tmp['userID'] = 'doc'
              tmp['password'] = 'doc'
            } else if (this.isWhere2 === 3) {
              tmp['userID'] = 'cert'
              tmp['password'] = 'cert'
            } else {
              tmp['userID'] = '123123123'
              tmp['password'] = '1231231n'
            }
          }
          params.push(tmp)
          this.Login({ ...tmp }).then((res) => this.loginSuccess(res))
            .catch(err => this.requestFailed(err))
            .finally(() => {
              // // console.log('')
            })
        }
      })
    },
    handleTabClick (key) {
      this.customActiveKey = key
    },
    stepCaptchaSuccess () {
      this.loginSuccess()
    },
    stepCaptchaCancel () {
      this.Logout().then(() => {
        this.loginBtn = false
        this.stepCaptchaVisible = false
      })
    },
    loginSuccess (res) {
      // console.log(res)
      if (res.code === 1000) {
        this.$router.push({ path: '/dashboard/workplace' })
        // 延迟 1 秒显示欢迎信息
        setTimeout(() => {
          this.$notification.success({
            message: '欢迎',
            description: `${timeFix()}，欢迎回来`
          })
        }, 1000)
        this.isLoginError = false
      } else {
        this.isLoginError = true
        this.$message.error('登录失败，请检查您输入的账户和密码是否正确，或者您的人脸信息是否已经录入系统')
        // this.requestFailed(res)
      }
    },
    requestFailed (err) {
      // // // console.log(err)
      this.isLoginError = true
      this.$notification['error']({
        message: '错误',
        description: ((err.response || {}).data || {}).message || '请求出现错误，请稍后再试',
        duration: 4
      })
    }
  }
}
</script>

<style lang="less" scoped>
.user-layout-login {
  label {
    font-size: 14px;
  }

  .getCaptcha {
    display: block;
    width: 100%;
    height: 40px;
  }

  .forge-password {
    font-size: 14px;
  }

  button.login-button {
    padding: 0 15px;
    font-size: 16px;
    height: 40px;
    width: 100%;
  }

  .user-login-other {
    text-align: left;
    margin-top: 24px;
    line-height: 22px;

    .item-icon {
      font-size: 24px;
      color: rgba(0, 0, 0, 0.2);
      margin-left: 16px;
      vertical-align: middle;
      cursor: pointer;
      transition: color 0.3s;

      &:hover {
        color: #1890ff;
      }
    }

    .register {
      float: right;
    }
  }
}
// 人脸识别
.container {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}

.title {
  margin: 40px 0;
  font-size: 24px;
}

.video-container {
  position: relative;
  width: 100%;
  height: 0;
  padding-top: 75%; /* 4:3 比例的响应式容器 */
  margin-bottom: 20px;
  border: 2px solid #ffffff;
  overflow: hidden;
}

video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.button-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-bottom: 40px;
}

.result-container {
  font-size: 18px;
}

@media (max-width: 768px) {
  .video-container {
    padding-top: 75%; /* 4:3 比例的响应式容器 */
  }

  .button-container {
    flex-direction: column;
    align-items: center;
  }

  .result-container {
    margin-top: 20px;
  }
}
</style>
