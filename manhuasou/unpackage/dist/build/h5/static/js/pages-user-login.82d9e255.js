(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-user-login"],{5331:function(t,n,i){"use strict";i.r(n);var e=i("88bd"),s=i("c61d");for(var a in s)"default"!==a&&function(t){i.d(n,t,(function(){return s[t]}))}(a);var u,o=i("f0c5"),r=Object(o["a"])(s["default"],e["b"],e["c"],!1,null,"1d08196b",null,!1,e["a"],u);n["default"]=r.exports},"88bd":function(t,n,i){"use strict";var e,s=function(){var t=this,n=t.$createElement,i=t._self._c||n;return i("v-uni-view",[i("v-uni-view",{staticClass:"input-box"},[i("v-uni-view",{staticClass:"input-item"},[i("v-uni-view",{staticClass:"input-label"},[t._v("手机号")]),i("v-uni-view",{staticClass:"input-body"},[i("v-uni-input",{staticClass:"input",attrs:{maxlength:"11",type:"number",placeholder:"请输入手机号"},model:{value:t.phone,callback:function(n){t.phone=n},expression:"phone"}})],1)],1),i("v-uni-view",{staticClass:"input-item"},[i("v-uni-view",{staticClass:"input-label"},[t._v("密码")]),i("v-uni-view",{staticClass:"input-body"},[i("v-uni-input",{staticClass:"input",staticStyle:{"margin-right":"50upx"},attrs:{type:"text",password:!!t.isHidePassword,placeholder:"请输入密码",maxlength:"20"},model:{value:t.password,callback:function(n){t.password=n},expression:"password"}}),i("v-uni-image",{staticClass:"eye",attrs:{src:t.isHidePassword?"/static/img/attention.png":"/static/img/attention_forbid.png"},on:{click:function(n){arguments[0]=n=t.$handleEvent(n),t.isHidePasswordClick.apply(void 0,arguments)}}})],1)],1),i("v-uni-view",{staticClass:"select"},[i("v-uni-navigator",{attrs:{url:"/pages/user/register","hover-class":"none"}},[t._v("注册")]),i("v-uni-navigator",{attrs:{url:"/pages/user/forget-pwd","hover-class":"none"}},[t._v("忘记密码？")])],1)],1),i("v-uni-button",{staticClass:"button",on:{click:function(n){arguments[0]=n=t.$handleEvent(n),t.submit.apply(void 0,arguments)}}},[t._v("登录")])],1)},a=[];i.d(n,"b",(function(){return s})),i.d(n,"c",(function(){return a})),i.d(n,"a",(function(){return e}))},c61d:function(t,n,i){"use strict";i.r(n);var e=i("edf7"),s=i.n(e);for(var a in e)"default"!==a&&function(t){i.d(n,t,(function(){return e[t]}))}(a);n["default"]=s.a},edf7:function(t,n,i){"use strict";Object.defineProperty(n,"__esModule",{value:!0}),n.default=void 0;var e=i("faa6"),s={data:function(){return{isHidePassword:!0,phone:"",password:""}},onLoad:function(){},methods:{isHidePasswordClick:function(){this.isHidePassword=!this.isHidePassword},submit:function(){(0,e.checkPhone)(this.phone)&&(0,e.checkPwd)(this.password)&&(this.$store.commit("update",["isLogin",!0]),uni.reLaunch({url:"/pages/my/index"}))}}};n.default=s},faa6:function(t,n,i){"use strict";function e(t){uni.showToast({icon:"none",title:t})}function s(t){var n=/^1\d{10}$/;return!!n.test(t)||(e("手机号格式错误"),!1)}function a(t){return t.length>=6||(e("密码必须大于6位"),!1)}function u(t){return 6==t.length||(e("验证码必须是6位数字"),!1)}function o(t){var n=/^\d{15}|\d{18}$/;return!!n.test(t)||(e("身份证必须是15或18位数字"),!1)}function r(t){var n=/^([1-9]{1})(\d{14}|\d{15}|\d{16}|\d{18})$/;return!!n.test(t)||(e("请输入正确的银行卡号"),!1)}Object.defineProperty(n,"__esModule",{value:!0}),n.toast=e,n.checkPhone=s,n.checkPwd=a,n.checkCode=u,n.checkIdCard=o,n.checkBankCard=r}}]);