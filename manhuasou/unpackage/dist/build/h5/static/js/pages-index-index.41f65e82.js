(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-index-index"],{"0080":function(t,e,i){"use strict";i.r(e);var n=i("5293"),A=i("6b79");for(var o in A)"default"!==o&&function(t){i.d(e,t,(function(){return A[t]}))}(o);i("6eb2");var a,s=i("f0c5"),r=Object(s["a"])(A["default"],n["b"],n["c"],!1,null,"08b04070",null,!1,n["a"],a);e["default"]=r.exports},"033b":function(t,e,i){"use strict";i("a9e3"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0,i("e39b");var n={data:function(){return{nav:[{name:"首页",icon:"",url:"/pages/index/index"},{name:"分类",icon:"",url:"/pages/list/index"},{name:"书架",icon:"",url:"/pages/bookshelf/index"},{name:"我的",icon:"",url:"/pages/my/index"}]}},methods:{},props:{navIndex:{type:Number,default:0}}};e.default=n},"07f1":function(t,e,i){"use strict";i.r(e);var n=i("033b"),A=i.n(n);for(var o in n)"default"!==o&&function(t){i.d(e,t,(function(){return n[t]}))}(o);e["default"]=A.a},"148e":function(t,e,i){"use strict";var n,A=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-uni-view",[i("v-uni-view",{staticClass:"nav_list"},t._l(t.nav,(function(e,n){return i("v-uni-view",{key:n,staticClass:"nav_item",style:{color:n==t.navIndex?"#FF8C00":"black"}},[i("v-uni-navigator",{attrs:{"animation-type":"pop-in","animation-duration":"300",url:e.url}},[i("v-uni-view",{staticClass:"control"},[i("v-uni-view",{staticClass:"iconfont"},[t._v(t._s(e.icon))]),i("v-uni-view",{staticStyle:{"margin-left":"-2rpx"}},[t._v(t._s(e.name))])],1)],1)],1)})),1)],1)},o=[];i.d(e,"b",(function(){return A})),i.d(e,"c",(function(){return o})),i.d(e,"a",(function(){return n}))},"1d01":function(t,e,i){var n=i("f812");"string"===typeof n&&(n=[[t.i,n,""]]),n.locals&&(t.exports=n.locals);var A=i("4f06").default;A("4b583de4",n,!0,{sourceMap:!1,shadowMode:!1})},"296a":function(t,e,i){var n=i("24fb");e=n(!1),e.push([t.i,'@charset "UTF-8";\r\n/**\r\n * 这里是uni-app内置的常用样式变量\r\n *\r\n * uni-app 官方扩展插件及插件市场（https://ext.dcloud.net.cn）上很多三方插件均使用了这些样式变量\r\n * 如果你是插件开发者，建议你使用scss预处理，并在插件代码中直接使用这些变量（无需 import 这个文件），方便用户通过搭积木的方式开发整体风格一致的App\r\n *\r\n */\r\n/**\r\n * 如果你是App开发者（插件使用者），你可以通过修改这些变量来定制自己的插件主题，实现自定义主题功能\r\n *\r\n * 如果你的项目同样使用了scss预处理，你也可以直接在你的 scss 代码中使用如下变量，同时无需 import 这个文件\r\n */\r\n/* 颜色变量 */\r\n/* 行为相关颜色 */\r\n/* 文字基本颜色 */\r\n/* 背景颜色 */\r\n/* 边框颜色 */\r\n/* 尺寸变量 */\r\n/* 文字尺寸 */\r\n/* 图片尺寸 */\r\n/* Border Radius */\r\n/* 水平间距 */\r\n/* 垂直间距 */\r\n/* 透明度 */\r\n/* 文章场景相关 */.index_top_nav[data-v-542f4dec]{padding-top:%?30?%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between;-webkit-box-align:center;-webkit-align-items:center;align-items:center;position:fixed;top:0;left:0;width:%?750?%;background:#fff;height:%?80?%;font-size:%?20?%;z-index:100}.index_top_nav .index_top_nav_item[data-v-542f4dec]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-align-content:center;align-content:center;height:%?80?%}.index_top_nav .index_top_nav_item .control[data-v-542f4dec]{margin-left:%?-15?%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-align-content:center;align-content:center;text-align:center}.menu_list[data-v-542f4dec]{padding-top:%?20?%;padding-bottom:%?20?%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;align-items:center;width:%?750?%;background:#fff;height:%?120?%;font-size:%?20?%;-webkit-box-shadow:0 %?2?% rgba(0,0,0,.06);box-shadow:0 %?2?% rgba(0,0,0,.06)}.menu_list .menu_item[data-v-542f4dec]{width:%?187.5?%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;align-items:center;height:%?120?%}.menu_list .menu_item .control[data-v-542f4dec]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-align-content:center;align-content:center;text-align:center}.book_info[data-v-542f4dec]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;flex-direction:column}.book_info .book_menu[data-v-542f4dec]{padding-left:%?40?%;padding-right:%?40?%;width:%?670?%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between;padding-top:%?20?%;padding-bottom:%?20?%}.book_info .book_menu .title[data-v-542f4dec]{font-size:%?36?%;font-weight:bolder}.book_info .book_menu .more[data-v-542f4dec]{display:-webkit-box;display:-webkit-flex;display:flex;font-size:%?20?%;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.book_info .book_list[data-v-542f4dec]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-flex-wrap:wrap;flex-wrap:wrap;padding-top:%?0?%}.book_info .book_list .book_item[data-v-542f4dec]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between;font-size:%?20?%;padding-left:%?35?%;width:%?320?%}.book_info .book_list .book_item .control[data-v-542f4dec]{width:%?330?%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;flex-direction:column}.book_info .book_list .book_item .control .book_name[data-v-542f4dec], .book_info .book_list .book_item .control .chapter_name[data-v-542f4dec]{padding-top:%?10?%;padding-bottom:%?10?%}',""]),t.exports=e},4730:function(t,e,i){"use strict";i.r(e);var n=i("8b11"),A=i.n(n);for(var o in n)"default"!==o&&function(t){i.d(e,t,(function(){return n[t]}))}(o);e["default"]=A.a},"4ff2":function(t,e,i){var n=i("f0e3");"string"===typeof n&&(n=[[t.i,n,""]]),n.locals&&(t.exports=n.locals);var A=i("4f06").default;A("3f6c5d52",n,!0,{sourceMap:!1,shadowMode:!1})},5293:function(t,e,i){"use strict";var n,A=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-uni-view",{staticClass:"serach"},[i("v-uni-view",{staticClass:"content",style:{"border-radius":t.radius+"px"}},[i("v-uni-view",{staticClass:"content-box",class:{center:2===t.mode}},[i("v-uni-text",{staticClass:"icon icon-serach"}),i("v-uni-input",{staticClass:"input",class:{center:!t.active&&2===t.mode},attrs:{placeholder:t.placeholder,"confirm-type":"search",focus:t.isFocus},on:{input:function(e){arguments[0]=e=t.$handleEvent(e),t.inputChange.apply(void 0,arguments)},confirm:function(e){arguments[0]=e=t.$handleEvent(e),t.triggerConfirm.apply(void 0,arguments)},focus:function(e){arguments[0]=e=t.$handleEvent(e),t.focus.apply(void 0,arguments)},blur:function(e){arguments[0]=e=t.$handleEvent(e),t.blur.apply(void 0,arguments)}},model:{value:t.inputVal,callback:function(e){t.inputVal=e},expression:"inputVal"}}),t.isDelShow?i("v-uni-text",{staticClass:"icon icon-del",on:{click:function(e){e.stopPropagation(),arguments[0]=e=t.$handleEvent(e),t.clear.apply(void 0,arguments)}}}):t._e()],1),i("v-uni-view",{directives:[{name:"show",rawName:"v-show",value:t.active&&t.show&&"inside"===t.button||t.isDelShow&&"inside"===t.button,expression:"(active&&show&&button === 'inside')||(isDelShow && button === 'inside')"}],staticClass:"serachBtn",on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.search.apply(void 0,arguments)}}},[t._v("搜索")])],1),"outside"===t.button?i("v-uni-view",{staticClass:"button",class:{active:t.show||t.active},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.search.apply(void 0,arguments)}}},[i("v-uni-view",{staticClass:"button-item"},[t._v(t._s(t.show?"搜索":t.searchName))])],1):t._e()],1)},o=[];i.d(e,"b",(function(){return A})),i.d(e,"c",(function(){return o})),i.d(e,"a",(function(){return n}))},"56de":function(t,e,i){var n=i("24fb");e=n(!1),e.push([t.i,'@charset "UTF-8";\r\n/**\r\n * 这里是uni-app内置的常用样式变量\r\n *\r\n * uni-app 官方扩展插件及插件市场（https://ext.dcloud.net.cn）上很多三方插件均使用了这些样式变量\r\n * 如果你是插件开发者，建议你使用scss预处理，并在插件代码中直接使用这些变量（无需 import 这个文件），方便用户通过搭积木的方式开发整体风格一致的App\r\n *\r\n */\r\n/**\r\n * 如果你是App开发者（插件使用者），你可以通过修改这些变量来定制自己的插件主题，实现自定义主题功能\r\n *\r\n * 如果你的项目同样使用了scss预处理，你也可以直接在你的 scss 代码中使用如下变量，同时无需 import 这个文件\r\n */\r\n/* 颜色变量 */\r\n/* 行为相关颜色 */\r\n/* 文字基本颜色 */\r\n/* 背景颜色 */\r\n/* 边框颜色 */\r\n/* 尺寸变量 */\r\n/* 文字尺寸 */\r\n/* 图片尺寸 */\r\n/* Border Radius */\r\n/* 水平间距 */\r\n/* 垂直间距 */\r\n/* 透明度 */\r\n/* 文章场景相关 */.serach[data-v-08b04070]{display:-webkit-box;display:-webkit-flex;display:flex;width:100%;-webkit-box-sizing:border-box;box-sizing:border-box;font-size:%?28?%}.serach .content[data-v-08b04070]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center;width:100%;height:%?60?%;background:#fff;overflow:hidden;-webkit-transition:all .2s linear;transition:all .2s linear;-webkit-border-radius:30px;border-radius:30px}.serach .content .content-box[data-v-08b04070]{width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.serach .content .content-box.center[data-v-08b04070]{-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center}.serach .content .content-box .icon[data-v-08b04070]{padding:0 %?15?%}.serach .content .content-box .icon.icon-del[data-v-08b04070]{font-size:%?38?%}.serach .content .content-box .icon.icon-del[data-v-08b04070]:before{content:"\\e644"}.serach .content .content-box .icon.icon-serach[data-v-08b04070]:before{content:"\\e61c"}.serach .content .content-box .input[data-v-08b04070]{width:100%;max-width:100%;line-height:%?60?%;height:%?60?%;-webkit-transition:all .2s linear;transition:all .2s linear}.serach .content .content-box .input.center[data-v-08b04070]{width:%?200?%}.serach .content .content-box .input.sub[data-v-08b04070]{width:auto;color:grey}.serach .content .serachBtn[data-v-08b04070]{height:100%;-webkit-flex-shrink:0;flex-shrink:0;padding:0 %?30?%;background:-webkit-gradient(linear,left top,right top,from(#ff9801),to(#ff570a));background:-webkit-linear-gradient(left,#ff9801,#ff570a);background:linear-gradient(90deg,#ff9801,#ff570a);line-height:%?60?%;color:#fff;-webkit-transition:all .3s;transition:all .3s}.serach .button[data-v-08b04070]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;position:relative;-webkit-flex-shrink:0;flex-shrink:0;width:0;-webkit-transition:all .2s linear;transition:all .2s linear;white-space:nowrap;overflow:hidden}.serach .button.active[data-v-08b04070]{padding-left:%?15?%;width:%?100?%}@font-face{font-family:iconfont;src:url("data:application/x-font-woff;charset=utf-8;base64,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")}.icon[data-v-08b04070]{font-family:iconfont;font-size:%?32?%;font-style:normal;color:#999}',""]),t.exports=e},5981:function(t,e,i){var n=i("296a");"string"===typeof n&&(n=[[t.i,n,""]]),n.locals&&(t.exports=n.locals);var A=i("4f06").default;A("bf8b3f2e",n,!0,{sourceMap:!1,shadowMode:!1})},"5cfc":function(t,e,i){"use strict";var n=i("5981"),A=i.n(n);A.a},"6b79":function(t,e,i){"use strict";i.r(e);var n=i("e420"),A=i.n(n);for(var o in n)"default"!==o&&function(t){i.d(e,t,(function(){return n[t]}))}(o);e["default"]=A.a},"6eb2":function(t,e,i){"use strict";var n=i("92d8"),A=i.n(n);A.a},"6fa4":function(t,e,i){var n=i("24fb");e=n(!1),e.push([t.i,'@font-face{font-family:iconfont;\r\n\t/* project id 1525278 */src:url(//at.alicdn.com/t/font_1525278_gcw28gvg8ps.eot);src:url(//at.alicdn.com/t/font_1525278_gcw28gvg8ps.eot#iefix) format("embedded-opentype"),url(//at.alicdn.com/t/font_1525278_gcw28gvg8ps.woff2) format("woff2"),url(//at.alicdn.com/t/font_1525278_gcw28gvg8ps.woff) format("woff"),url(//at.alicdn.com/t/font_1525278_gcw28gvg8ps.ttf) format("truetype"),url(//at.alicdn.com/t/font_1525278_gcw28gvg8ps.svg#iconfont) format("svg")}.iconfont{font-family:iconfont!important;font-size:18px;font-style:normal;-webkit-font-smoothing:antialiased;-webkit-text-stroke-width:.2px;-moz-osx-font-smoothing:grayscale}',""]),t.exports=e},"7e6a":function(t,e,i){"use strict";i.r(e);var n=i("b5cd"),A=i("8fef");for(var o in A)"default"!==o&&function(t){i.d(e,t,(function(){return A[t]}))}(o);i("5cfc");var a,s=i("f0c5"),r=Object(s["a"])(A["default"],n["b"],n["c"],!1,null,"542f4dec",null,!1,n["a"],a);e["default"]=r.exports},8192:function(t,e,i){"use strict";i.r(e);var n=i("a2a4"),A=i("4730");for(var o in A)"default"!==o&&function(t){i.d(e,t,(function(){return A[t]}))}(o);i("bb9f");var a,s=i("f0c5"),r=Object(s["a"])(A["default"],n["b"],n["c"],!1,null,"7a74f770",null,!1,n["a"],a);e["default"]=r.exports},8248:function(t,e,i){"use strict";var n=i("1d01"),A=i.n(n);A.a},"8b11":function(t,e,i){"use strict";var n=i("ee27");i("c975"),i("a434"),i("ac1f"),i("5319"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var A=n(i("0080")),o={data:function(){return{defaultKeyword:"",keyword:"",oldKeywordList:[],hotKeywordList:[],keywordList:[],forbid:"",isShowKeywordList:!1}},onLoad:function(){this.init()},components:{mSearch:A.default},methods:{init:function(){this.loadDefaultKeyword(),this.loadOldKeyword(),this.loadHotKeyword()},blur:function(){uni.hideKeyboard()},loadDefaultKeyword:function(){this.defaultKeyword="默认关键字"},loadOldKeyword:function(){var t=this;uni.getStorage({key:"OldKeys",success:function(e){var i=JSON.parse(e.data);t.oldKeywordList=i}})},loadHotKeyword:function(){this.hotKeywordList=["键盘","鼠标","显示器","电脑主机","蓝牙音箱","笔记本电脑","鼠标垫","USB","USB3.0"]},inputChange:function(t){var e=this,i=t.detail?t.detail.value:t;if(!i)return this.keywordList=[],void(this.isShowKeywordList=!1);this.isShowKeywordList=!0,uni.request({url:"http://192.168.2.100/getKeyword/"+i,success:function(t){e.keywordList=[],e.keywordList=t.data}})},drawCorrelativeKeyword:function(t,e){for(var i=t.length,n=[],A=0;A<i;A++){var o=t[A],a=o[0].replace(e,"<span style='color: #9f9f9f;'>"+e+"</span>");a="<div>"+a+"</div>";var s={keyword:o[0],htmlStr:a};n.push(s)}return n},setKeyword:function(t){this.keyword=this.keywordList[t].keyword},oldDelete:function(){var t=this;uni.showModal({content:"确定清除历史搜索记录？",success:function(e){e.confirm?(console.log("用户点击确定"),t.oldKeywordList=[],uni.removeStorage({key:"OldKeys"})):e.cancel&&console.log("用户点击取消")}})},hotToggle:function(){this.forbid=this.forbid?"":"_forbid"},doSearch:function(t,e){t=!1===t?this.keyword:t,this.keyword=t,this.saveKeyword(t),uni.showToast({title:t,icon:"none",duration:2e3}),uni.navigateTo({url:"/pages/chapter/index?id="+e})},saveKeyword:function(t){var e=this;uni.getStorage({key:"OldKeys",success:function(i){var n=JSON.parse(i.data),A=n.indexOf(t);-1==A?n.unshift(t):(n.splice(A,1),n.unshift(t)),n.length>10&&n.pop(),uni.setStorage({key:"OldKeys",data:JSON.stringify(n)}),e.oldKeywordList=n},fail:function(i){var n=[t];uni.setStorage({key:"OldKeys",data:JSON.stringify(n)}),e.oldKeywordList=n}})}}};e.default=o},"8fef":function(t,e,i){"use strict";i.r(e);var n=i("b760"),A=i.n(n);for(var o in n)"default"!==o&&function(t){i.d(e,t,(function(){return n[t]}))}(o);e["default"]=A.a},"92d8":function(t,e,i){var n=i("56de");"string"===typeof n&&(n=[[t.i,n,""]]),n.locals&&(t.exports=n.locals);var A=i("4f06").default;A("226b7aa6",n,!0,{sourceMap:!1,shadowMode:!1})},a2a4:function(t,e,i){"use strict";var n,A=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-uni-view",{staticClass:"content"},[i("v-uni-view",{staticClass:"search-box"},[i("mSearch",{staticClass:"mSearch-input-box",attrs:{mode:2,button:"inside",placeholder:t.defaultKeyword},on:{search:function(e){arguments[0]=e=t.$handleEvent(e),t.doSearch(!1)},input:function(e){arguments[0]=e=t.$handleEvent(e),t.inputChange.apply(void 0,arguments)},confirm:function(e){arguments[0]=e=t.$handleEvent(e),t.doSearch(!1)}},model:{value:t.keyword,callback:function(e){t.keyword=e},expression:"keyword"}})],1),i("v-uni-view",{staticClass:"search-keyword"},[i("v-uni-scroll-view",{directives:[{name:"show",rawName:"v-show",value:t.isShowKeywordList,expression:"isShowKeywordList"}],staticClass:"keyword-list-box",attrs:{"scroll-y":!0}},[t._l(t.keywordList,(function(e,n){return[i("v-uni-navigator",[i("v-uni-view",{staticClass:"keyword-entry",attrs:{"hover-class":"keyword-entry-tap"}},[i("v-uni-view",{staticClass:"keyword-text",on:{click:function(i){i.stopPropagation(),arguments[0]=i=t.$handleEvent(i),t.doSearch(e.fields.book_name,e.pk)}}},[i("v-uni-rich-text",{attrs:{nodes:e.fields.book_name}})],1),i("v-uni-view",{staticClass:"keyword-img",on:{click:function(i){i.stopPropagation(),arguments[0]=i=t.$handleEvent(i),t.setKeyword(e.fields.book_name)}}},[i("v-uni-image",{attrs:{src:"/static/HM-search/back.png"}})],1)],1)],1)]}))],2),i("v-uni-scroll-view",{directives:[{name:"show",rawName:"v-show",value:!t.isShowKeywordList,expression:"!isShowKeywordList"}],staticClass:"keyword-box",attrs:{"scroll-y":!0}},[t.oldKeywordList.length>0?i("v-uni-view",{staticClass:"keyword-block"},[i("v-uni-view",{staticClass:"keyword-list-header"},[i("v-uni-view",[t._v("历史搜索")]),i("v-uni-view",[i("v-uni-image",{attrs:{src:"/static/HM-search/delete.png"},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.oldDelete.apply(void 0,arguments)}}})],1)],1),i("v-uni-view",{staticClass:"keyword"},t._l(t.oldKeywordList,(function(e,n){return i("v-uni-view",{key:n,on:{click:function(i){arguments[0]=i=t.$handleEvent(i),t.doSearch(e,n)}}},[t._v(t._s(e))])})),1)],1):t._e(),i("v-uni-view",{staticClass:"keyword-block"},[i("v-uni-view",{staticClass:"keyword-list-header"},[i("v-uni-view",[t._v("热门搜索")]),i("v-uni-view",[i("v-uni-image",{attrs:{src:"/static/HM-search/attention"+t.forbid+".png"},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.hotToggle.apply(void 0,arguments)}}})],1)],1),""==t.forbid?i("v-uni-view",{staticClass:"keyword"},t._l(t.hotKeywordList,(function(e,n){return i("v-uni-view",{key:n,on:{click:function(i){arguments[0]=i=t.$handleEvent(i),t.doSearch(e,n)}}},[t._v(t._s(e))])})),1):i("v-uni-view",{staticClass:"hide-hot-tis"},[i("v-uni-view",[t._v("当前搜热门搜索已隐藏")])],1)],1)],1)],1)],1)},o=[];i.d(e,"b",(function(){return A})),i.d(e,"c",(function(){return o})),i.d(e,"a",(function(){return n}))},a3b3:function(t,e,i){"use strict";i.r(e);var n=i("148e"),A=i("07f1");for(var o in A)"default"!==o&&function(t){i.d(e,t,(function(){return A[t]}))}(o);i("8248");var a,s=i("f0c5"),r=Object(s["a"])(A["default"],n["b"],n["c"],!1,null,"568a8e86",null,!1,n["a"],a);e["default"]=r.exports},b5cd:function(t,e,i){"use strict";var n,A=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-uni-view",[0==t.showSearch?[i("v-uni-view",{staticClass:"index_top_nav"},[0==t.sex?i("v-uni-view",{staticClass:"index_top_nav_item iconfont",staticStyle:{"z-index":"100","margin-top":"-18upx","padding-left":"30upx","font-size":"67upx",color:"pink"},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.sex=1}}},[t._v(t._s(0==t.sex?"":""))]):t._e(),0==t.sex?i("v-uni-view",{staticClass:"index_top_nav_item iconfont",staticStyle:{"margin-left":"-185upx","margin-top":"-20upx","padding-left":"30upx","font-size":"75upx",color:"#007AFF"},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.sex=1}}},[t._v(t._s(0==!t.sex?"":""))]):t._e(),1==t.sex?i("v-uni-view",{staticClass:"index_top_nav_item iconfont",staticStyle:{"z-index":"100","margin-top":"-25upx","padding-left":"30upx","font-size":"75upx",color:"#007AFF"},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.sex=0}}},[t._v(t._s(0==t.sex?"":""))]):t._e(),1==t.sex?i("v-uni-view",{staticClass:"index_top_nav_item iconfont",staticStyle:{"margin-top":"-16upx","padding-left":"30upx","font-size":"67upx",color:"pink","margin-left":"-185upx"},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.sex=0}}},[t._v(t._s(0==!t.sex?"":""))]):t._e(),t._l(t.navList,(function(e,n){return i("v-uni-view",{key:n,staticClass:"index_top_nav_item",style:{color:n==t.navIndex?"#FF8C00":""},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.navIndex=n}}},[i("v-uni-view",{staticClass:"control"},[i("v-uni-view",{staticStyle:{"font-size":"36upx"}},[t._v(t._s(e.name))]),i("v-uni-view",{staticClass:"iconfont",staticStyle:{"margin-top":"-12upx"}},[t._v("")])],1)],1)})),i("v-uni-view",{staticClass:"index_top_nav_item iconfont",staticStyle:{color:"#FF8C00","margin-right":"20rpx"},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.setShowsearch()}}},[t._v("")])],2),i("v-uni-swiper",{staticStyle:{height:"400upx","padding-top":"100upx"},attrs:{"indicator-dots":""}},t._l(t.bookList,(function(t){return i("v-uni-swiper-item",{key:t.pk},[i("v-uni-image",{staticStyle:{width:"750upx"},attrs:{src:t.fields.cover_url}})],1)})),1),i("v-uni-view",{staticClass:"menu_list"},t._l(t.nav,(function(e,n){return i("v-uni-view",{key:n,staticClass:"menu_item",style:{color:n==t.navIndex?"#FF8C00":""},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.navIndex=n}}},[i("v-uni-navigator",{attrs:{url:e.url}},[i("v-uni-view",{staticClass:"control"},[i("v-uni-view",{staticClass:"iconfont"},[t._v(t._s(e.icon))]),i("v-uni-view",{staticStyle:{"margin-left":"-2upx"}},[t._v(t._s(e.name))])],1)],1)],1)})),1),t._l(4,(function(e){return i("v-uni-view",{key:e,staticClass:"book_info"},[i("v-uni-view",{staticClass:"book_menu"},[i("v-uni-view",{staticClass:"title"},[t._v("客栈精品")]),i("v-uni-navigator",{attrs:{url:"../list/index","open-type":"switchTab"}},[i("v-uni-view",{staticClass:"more"},[t._v("更多")])],1)],1),i("v-uni-view",{staticClass:"book_list"},t._l(t.bookList,(function(e,n){return i("v-uni-view",{key:n,staticClass:"book_item"},[i("v-uni-navigator",{attrs:{url:"../chapter/index?id="+e.pk}},[i("v-uni-view",{staticClass:"control"},[i("v-uni-view",[i("v-uni-image",{staticStyle:{width:"320upx"},attrs:{mode:"widthFix",src:e.fields.cover_url}})],1),i("v-uni-view",{staticClass:"book_name"},[t._v(t._s(e.fields.book_name))]),i("v-uni-view",{staticClass:"chapter_name"},[t._v(t._s(e.fields.last_chapter))])],1)],1)],1)})),1)],1)}))]:[i("v-search")]],2)},o=[];i.d(e,"b",(function(){return A})),i.d(e,"c",(function(){return o})),i.d(e,"a",(function(){return n}))},b760:function(t,e,i){"use strict";var n=i("ee27");Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0,i("e39b");var A=n(i("a3b3")),o=n(i("8192")),a={data:function(){return{navList:[{name:"推荐",url:""},{name:"更新",url:""}],navIndex:0,nav:[{name:"排行榜",icon:";",url:"/pages/index/index"},{name:"VIP专区",icon:"",url:"/pages/list/index"},{name:"书单",icon:"",url:"/pages/bookshelf/index"},{name:"积分商城",icon:"",url:"/pages/my/index"}],sex:0,showSearch:!1,bookList:[]}},components:{"v-nav":A.default,"v-search":o.default},methods:{goToSearch:function(){console.log(123)},setShowsearch:function(){this.showSearch=!0,uni.hideTabBar({})}},beforeCreate:function(){var t=this;uni.request({url:"http://192.168.2.100/showBooklist/0/12",data:{},header:{},success:function(e){t.bookList=e.data}})}};e.default=a},bb9f:function(t,e,i){"use strict";var n=i("4ff2"),A=i.n(n);A.a},e39b:function(t,e,i){var n=i("6fa4");"string"===typeof n&&(n=[[t.i,n,""]]),n.locals&&(t.exports=n.locals);var A=i("4f06").default;A("0343fbf9",n,!0,{sourceMap:!1,shadowMode:!1})},e420:function(t,e,i){"use strict";i("a9e3"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var n={props:{mode:{value:Number,default:1},placeholder:{value:String,default:"请输入搜索内容"},value:{type:String,default:!1},button:{value:String,default:"outside"},show:{value:Boolean,default:!0},radius:{value:String,default:60}},data:function(){return{active:!1,inputVal:"",searchName:"取消",isDelShow:!1,isFocus:!0}},methods:{triggerConfirm:function(){this.$emit("confirm",!1)},inputChange:function(t){var e=t.detail.value;this.$emit("input",e),this.inputVal&&(this.isDelShow=!0)},focus:function(){this.active=!0,this.inputVal&&(this.isDelShow=!0)},blur:function(){console.log("blur"),this.isFocus=!1,this.inputVal||(this.active=!1)},clear:function(){uni.hideKeyboard(),this.isFocus=!1,this.inputVal="",this.active=!1,this.$emit("input","")},getFocus:function(){this.isFocus||(this.isFocus=!0)},search:function(){if(!this.inputVal&&!this.show&&"取消"==this.searchName)return uni.hideKeyboard(),this.isFocus=!1,void(this.active=!1);console.log(this.inputVal),this.$emit("search",this.inputVal?this.inputVal:this.placeholder)}},watch:{inputVal:function(t){t?this.searchName="搜索":(this.searchName="取消",this.isDelShow=!1)},value:function(t){this.inputVal=t}}};e.default=n},f0e3:function(t,e,i){var n=i("24fb");e=n(!1),e.push([t.i,'@charset "UTF-8";\r\n/**\r\n * 这里是uni-app内置的常用样式变量\r\n *\r\n * uni-app 官方扩展插件及插件市场（https://ext.dcloud.net.cn）上很多三方插件均使用了这些样式变量\r\n * 如果你是插件开发者，建议你使用scss预处理，并在插件代码中直接使用这些变量（无需 import 这个文件），方便用户通过搭积木的方式开发整体风格一致的App\r\n *\r\n */\r\n/**\r\n * 如果你是App开发者（插件使用者），你可以通过修改这些变量来定制自己的插件主题，实现自定义主题功能\r\n *\r\n * 如果你的项目同样使用了scss预处理，你也可以直接在你的 scss 代码中使用如下变量，同时无需 import 这个文件\r\n */\r\n/* 颜色变量 */\r\n/* 行为相关颜色 */\r\n/* 文字基本颜色 */\r\n/* 背景颜色 */\r\n/* 边框颜色 */\r\n/* 尺寸变量 */\r\n/* 文字尺寸 */\r\n/* 图片尺寸 */\r\n/* Border Radius */\r\n/* 水平间距 */\r\n/* 垂直间距 */\r\n/* 透明度 */\r\n/* 文章场景相关 */uni-view[data-v-7a74f770]{display:block}.search-box[data-v-7a74f770]{width:95%;background-color:#f2f2f2;padding:%?15?% 2.5%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between;position:-webkit-sticky;position:sticky;top:0}.search-box .mSearch-input-box[data-v-7a74f770]{width:100%}.search-box .input-box[data-v-7a74f770]{width:85%;-webkit-flex-shrink:1;flex-shrink:1;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.search-box .search-btn[data-v-7a74f770]{width:15%;margin:0 0 0 2%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;align-items:center;-webkit-flex-shrink:0;flex-shrink:0;font-size:%?28?%;color:#fff;background:-webkit-gradient(linear,left top,right top,from(#ff9801),to(#ff570a));background:-webkit-linear-gradient(left,#ff9801,#ff570a);background:linear-gradient(90deg,#ff9801,#ff570a);-webkit-border-radius:%?60?%;border-radius:%?60?%}.search-box .input-box > uni-input[data-v-7a74f770]{width:100%;height:%?60?%;font-size:%?32?%;border:0;-webkit-border-radius:%?60?%;border-radius:%?60?%;-webkit-appearance:none;-moz-appearance:none;appearance:none;padding:0 3%;margin:0;background-color:#fff}.placeholder-class[data-v-7a74f770]{color:#9e9e9e}.search-keyword[data-v-7a74f770]{width:100%;background-color:#f2f2f2}.keyword-list-box[data-v-7a74f770]{height:calc(100vh - %?110?%);padding-top:%?10?%;-webkit-border-radius:%?20?% %?20?% 0 0;border-radius:%?20?% %?20?% 0 0;background-color:#fff}.keyword-entry-tap[data-v-7a74f770]{background-color:#eee}.keyword-entry[data-v-7a74f770]{width:94%;height:%?80?%;margin:0 3%;font-size:%?30?%;color:#333;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between;-webkit-box-align:center;-webkit-align-items:center;align-items:center;border-bottom:solid %?1?% #e7e7e7}.keyword-entry uni-image[data-v-7a74f770]{width:%?60?%;height:%?60?%}.keyword-entry .keyword-text[data-v-7a74f770],\r\n.keyword-entry .keyword-img[data-v-7a74f770]{height:%?80?%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.keyword-entry .keyword-text[data-v-7a74f770]{width:90%}.keyword-entry .keyword-img[data-v-7a74f770]{width:10%;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center}.keyword-box[data-v-7a74f770]{height:calc(100vh - %?110?%);-webkit-border-radius:%?20?% %?20?% 0 0;border-radius:%?20?% %?20?% 0 0;background-color:#fff}.keyword-box .keyword-block[data-v-7a74f770]{padding:%?10?% 0}.keyword-box .keyword-block .keyword-list-header[data-v-7a74f770]{width:94%;padding:%?10?% 3%;font-size:%?27?%;color:#333;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between}.keyword-box .keyword-block .keyword-list-header uni-image[data-v-7a74f770]{width:%?40?%;height:%?40?%}.keyword-box .keyword-block .keyword[data-v-7a74f770]{width:94%;padding:3px 3%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-flex-flow:wrap;flex-flow:wrap;-webkit-box-pack:start;-webkit-justify-content:flex-start;justify-content:flex-start}.keyword-box .keyword-block .hide-hot-tis[data-v-7a74f770]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;font-size:%?28?%;color:#6b6b6b}.keyword-box .keyword-block .keyword > uni-view[data-v-7a74f770]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;align-items:center;-webkit-border-radius:%?60?%;border-radius:%?60?%;padding:0 %?20?%;margin:%?10?% %?20?% %?10?% 0;height:%?60?%;font-size:%?28?%;background-color:#f2f2f2;color:#6b6b6b}',""]),t.exports=e},f812:function(t,e,i){var n=i("24fb");e=n(!1),e.push([t.i,".nav_list[data-v-568a8e86]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;align-items:center;position:fixed;bottom:0;left:0;width:%?750?%;background:#fff;height:%?120?%;font-size:%?20?%}.nav_item[data-v-568a8e86]{width:%?187.5?%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;align-items:center;height:%?120?%}.control[data-v-568a8e86]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-align-content:center;align-content:center;text-align:center}",""]),t.exports=e}}]);