(window.webpackJsonp=window.webpackJsonp||[]).push([[3],{377:function(t,r,n){"use strict";n.r(r);var e=n(46),o=n(52),c=n.n(o),l=n(169),d=n(389),v=n(395),f=n(167),m=n(139),h=n(390),component=Object(e.a)({},(function(){var t=this,r=t.$createElement,n=t._self._c||r;return n("v-container",{staticClass:"py-0",staticStyle:{"margin-top":"-192px"}},[n("v-row",{attrs:{justify:"center"}},[n("v-avatar",{staticClass:"elevation-15",attrs:{width:"50%",height:"auto","max-width":"220"}},[n("v-img",{attrs:{src:"/images/profile.jpg"}})],1)],1),t._v(" "),n("v-row",{attrs:{justify:"center"}},[n("v-col",{staticClass:"text-center",attrs:{cols:"auto"}},[n("h1",[n("span",{staticClass:"font-weight-light tw-text-3xl"},[t._v("Justin ")]),t._v(" "),n("span",{staticClass:"indigo--text tw-text-3xl"},[t._v("Swaney")])]),t._v(" "),n("p",[n("em",[t._v("Scientist, Developer, Engineer")]),t._v(" "),n("br"),t._v(" "),n("v-icon",{staticClass:"px-5",attrs:{color:"indigo lighten-2"}},[t._v("mdi-microscope")]),t._v(" "),n("v-icon",{staticClass:"px-5",attrs:{color:"indigo lighten-2"}},[t._v("mdi-laptop-windows")]),t._v(" "),n("v-icon",{staticClass:"px-5",attrs:{color:"indigo lighten-2"}},[t._v("mdi-flask")])],1)])],1)],1)}),[],!1,null,null,null);r.default=component.exports;c()(component,{VAvatar:l.a,VCol:d.a,VContainer:v.a,VIcon:f.a,VImg:m.a,VRow:h.a})},392:function(t,r,n){"use strict";n.r(r);n(68);var e=n(15),o={components:{HomeAvatar:n(377).default},asyncData:function(t){return Object(e.a)(regeneratorRuntime.mark((function r(){var n,e;return regeneratorRuntime.wrap((function(r){for(;;)switch(r.prev=r.next){case 0:return n=t.$content,r.next=3,n("about").fetch();case 3:return e=r.sent,r.abrupt("return",{about:e});case 5:case"end":return r.stop()}}),r)})))()}},c=n(46),l=n(52),d=n.n(l),v=n(172),f=n(395),component=Object(c.a)(o,(function(){var t=this.$createElement,r=this._self._c||t;return r("v-container",{attrs:{justify:"center"}},[r("HomeAvatar"),this._v(" "),r("v-card",{staticClass:"pa-2 mx-auto",attrs:{flat:"","max-width":"500px",color:"grey lighten-4"}},[r("nuxt-content",{staticClass:"tw-prose",attrs:{document:this.about}})],1)],1)}),[],!1,null,null,null);r.default=component.exports;d()(component,{HomeAvatar:n(377).default}),d()(component,{VCard:v.a,VContainer:f.a})},395:function(t,r,n){"use strict";n(23),n(67),n(66),n(55),n(248),n(375),n(69),n(57);var e=n(1);var o,c=n(105);r.a=(o="container",e.a.extend({name:"v-".concat(o),functional:!0,props:{id:String,tag:{type:String,default:"div"}},render:function(t,r){var n=r.props,data=r.data,e=r.children;data.staticClass="".concat(o," ").concat(data.staticClass||"").trim();var c=data.attrs;if(c){data.attrs={};var l=Object.keys(c).filter((function(t){if("slot"===t)return!1;var r=c[t];return t.startsWith("data-")?(data.attrs[t]=r,!1):r||"string"==typeof r}));l.length&&(data.staticClass+=" ".concat(l.join(" ")))}return n.id&&(data.domProps=data.domProps||{},data.domProps.id=n.id),t(n.tag,data,e)}})).extend({name:"v-container",functional:!0,props:{id:String,tag:{type:String,default:"div"},fluid:{type:Boolean,default:!1}},render:function(t,r){var n,e=r.props,data=r.data,o=r.children,l=data.attrs;return l&&(data.attrs={},n=Object.keys(l).filter((function(t){if("slot"===t)return!1;var r=l[t];return t.startsWith("data-")?(data.attrs[t]=r,!1):r||"string"==typeof r}))),e.id&&(data.domProps=data.domProps||{},data.domProps.id=e.id),t(e.tag,Object(c.a)(data,{staticClass:"container",class:Array({"container--fluid":e.fluid}).concat(n||[])}),o)}})}}]);