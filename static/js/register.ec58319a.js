(function(e){function t(t){for(var r,s,c=t[0],i=t[1],l=t[2],p=0,d=[];p<c.length;p++)s=c[p],Object.prototype.hasOwnProperty.call(n,s)&&n[s]&&d.push(n[s][0]),n[s]=0;for(r in i)Object.prototype.hasOwnProperty.call(i,r)&&(e[r]=i[r]);u&&u(t);while(d.length)d.shift()();return o.push.apply(o,l||[]),a()}function a(){for(var e,t=0;t<o.length;t++){for(var a=o[t],r=!0,c=1;c<a.length;c++){var i=a[c];0!==n[i]&&(r=!1)}r&&(o.splice(t--,1),e=s(s.s=a[0]))}return e}var r={},n={register:0},o=[];function s(t){if(r[t])return r[t].exports;var a=r[t]={i:t,l:!1,exports:{}};return e[t].call(a.exports,a,a.exports,s),a.l=!0,a.exports}s.m=e,s.c=r,s.d=function(e,t,a){s.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:a})},s.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.t=function(e,t){if(1&t&&(e=s(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var a=Object.create(null);if(s.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)s.d(a,r,function(t){return e[t]}.bind(null,r));return a},s.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return s.d(t,"a",t),t},s.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},s.p="/static/";var c=window["webpackJsonp"]=window["webpackJsonp"]||[],i=c.push.bind(c);c.push=t,c=c.slice();for(var l=0;l<c.length;l++)t(c[l]);var u=i;o.push([2,"chunk-vendors"]),a()})({2:function(e,t,a){e.exports=a("a372")},"9fc4":function(e,t,a){"use strict";var r={accounts:{login:"/accounts/register/",register:"/accounts/register/"},bot_data:{index:"/botdata/",laisha2:{material:"/botdata/laisha2/material/"},version_info:{get:"/botdata/version_info/"}}};t["a"]=r},a372:function(e,t,a){"use strict";a.r(t);a("e260"),a("e6cf"),a("cca6"),a("a79d");var r=a("2b0e"),n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-app",[a("v-main",[a("v-container",{attrs:{fluid:""}},[a("Register")],1)],1)],1)},o=[],s=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-container",[a("v-row",{attrs:{align:"center",justify:"center"}},[a("v-col",{attrs:{cols:"6"}},[a("v-form",[a("v-card",{attrs:{elevation:"0"}},[a("h1",{staticClass:"text-center"},[e._v("注册账号")]),a("v-row",[a("v-col",[a("v-text-field",{attrs:{label:"账号"},model:{value:e.username,callback:function(t){e.username=t},expression:"username"}})],1)],1),a("v-row",[a("v-col",[a("v-text-field",{attrs:{label:"昵称"},model:{value:e.nickname,callback:function(t){e.nickname=t},expression:"nickname"}})],1)],1),a("v-row",[a("v-col",[a("v-text-field",{attrs:{label:"邮箱"},model:{value:e.email,callback:function(t){e.email=t},expression:"email"}})],1)],1),a("v-row",[a("v-col",[a("v-text-field",{attrs:{label:"密码",type:"password"},model:{value:e.password1,callback:function(t){e.password1=t},expression:"password1"}})],1)],1),a("v-row",[a("v-col",[a("v-text-field",{attrs:{label:"确认密码",type:"password"},model:{value:e.password2,callback:function(t){e.password2=t},expression:"password2"}})],1)],1),a("v-card-actions",[a("v-spacer"),a("v-btn",{on:{click:e.recaptcha}},[e._v("submit")])],1)],1)],1)],1)],1)],1)},c=[],i=a("1da1"),l=(a("96cf"),a("bc3a")),u=a.n(l),p=a("9fc4"),d={data:function(){return{nickname:null,username:null,email:null,password1:null,password2:null}},methods:{recaptcha:function(){var e=this;return Object(i["a"])(regeneratorRuntime.mark((function t(){var a;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:if(!(e.nickname&&e.username&&e.email&&e.password1&&e.password2)){t.next=13;break}if(e.password1!=e.password2){t.next=10;break}return t.next=4,e.$recaptchaLoaded();case 4:return t.next=6,e.$recaptcha("register");case 6:a=t.sent,e.register(a),t.next=11;break;case 10:alert("输入的密码不一致！");case 11:t.next=14;break;case 13:alert("参数不能为空！");case 14:case"end":return t.stop()}}),t)})))()},register:function(e){var t={username:this.username,nickname:this.nickname,email:this.email,password1:this.password1,password2:this.password2,token:e};u.a.post(p["a"].accounts.register,t).then((function(e){console.log(e.data)})),console.log(e)}}},f=d,v=a("2877"),m=a("6544"),b=a.n(m),h=a("8336"),w=a("b0af"),g=a("99d9"),x=a("62ad"),k=a("a523"),y=a("4bd4"),j=a("0fd9"),O=a("2fa4"),_=a("8654"),V=Object(v["a"])(f,s,c,!1,null,null,null),C=V.exports;b()(V,{VBtn:h["a"],VCard:w["a"],VCardActions:g["a"],VCol:x["a"],VContainer:k["a"],VForm:y["a"],VRow:j["a"],VSpacer:O["a"],VTextField:_["a"]});var R={data:function(){return{}},components:{Register:C}},P=R,S=a("7496"),A=a("f6c4"),M=Object(v["a"])(P,n,o,!1,null,null,null),T=M.exports;b()(M,{VApp:S["a"],VContainer:k["a"],VMain:A["a"]});var $=a("f309");r["a"].use($["a"]);var B=new $["a"]({}),E=(a("ac1f"),a("d3b7"),function(e){var t=/csrftoken=([\w]+)[;]?/g;return t.exec(e)[1]});u.a.interceptors.request.use((function(e){var t=document.cookie;return t&&"post"==e.method&&(e.headers["X-CSRFToken"]=E(t)),e}),(function(e){return Promise.reject(e)}));var F=a("760d"),L=a("d645");r["a"].use(F["VueReCaptcha"],{siteKey:L["a"].recaptcha,loaderOptions:{useRecaptchaNet:!0}}),r["a"].config.productionTip=!1,new r["a"]({vuetify:B,render:function(e){return e(T)}}).$mount("#app")},d645:function(e,t,a){"use strict";var r={recaptcha:"6LdMUIQaAAAAAB3Bj_aRVji7Ln2StxjKYEC2XYO8"};t["a"]=r}});
//# sourceMappingURL=register.ec58319a.js.map