import{u as L,a as z,r as x,b as m,o as E,c as l,d as u,e as f,f as a,F as K,g as M,h as g,w as o,i as N,n as T,t as j,j as e,k,p as A,l as D,E as H}from"./index-48a4c1cb.js";import{_ as R}from"./_plugin-vue_export-helper-c27b6911.js";const b=p=>(A("data-v-90ff4561"),p=p(),D(),p),$={id:"loginView"},q={class:"loginView_content"},G=b(()=>a("div",{class:"title"},"登录",-1)),J={class:"form"},O={class:"form-selector"},P=["onClick"],Q={class:"subLoginBtns"},W=b(()=>a("div",{class:"btn"},null,-1)),X={__name:"index",setup(p){const C=L(),U=z(),r=x(""),v=m(["账户密码登录","手机号登录"]),n=m({userName:"",password:""}),_=m({userName:"",password:""});E(()=>{r.value=v[0]});const V=x(!1),B=()=>{U.loginApi({userName:n.userName,password:n.password}).then(c=>{c?C.push({path:"/chat"}):H.error("登录失败，请确认帐号和密码")})};return(c,t)=>{const S=l("User"),h=l("el-icon"),i=l("el-input"),d=l("el-form-item"),F=l("Key"),I=l("el-checkbox"),y=l("el-button"),w=l("el-form");return u(),f("div",$,[a("div",q,[G,a("div",J,[a("div",O,[(u(!0),f(K,null,M(v,s=>(u(),f("div",{class:T(["selector-item",r.value===s?"selector-item__active":""])},[a("span",{onClick:Y=>r.value=s},j(s),9,P)],2))),256))]),r.value==="账户密码登录"?(u(),g(w,{key:0},{default:o(()=>[e(d,null,{default:o(()=>[e(i,{modelValue:n.userName,"onUpdate:modelValue":t[0]||(t[0]=s=>n.userName=s),placeholder:"账户"},{prefix:o(()=>[e(h,null,{default:o(()=>[e(S)]),_:1})]),_:1},8,["modelValue"])]),_:1}),e(d,null,{default:o(()=>[e(i,{modelValue:n.password,"onUpdate:modelValue":t[1]||(t[1]=s=>n.password=s),type:"password",placeholder:"密码"},{prefix:o(()=>[e(h,null,{default:o(()=>[e(F)]),_:1})]),_:1},8,["modelValue"])]),_:1}),e(d,{style:{height:"40px"}},{default:o(()=>[a("div",Q,[e(I,{modelValue:V.value,"onUpdate:modelValue":t[2]||(t[2]=s=>V.value=s),label:"自动登录",size:"large"},null,8,["modelValue"]),e(y,{text:"",type:"primary",style:{width:"80px"}},{default:o(()=>[k("忘记密码")]),_:1})])]),_:1}),e(d,null,{default:o(()=>[e(y,{type:"primary",style:{"font-size":"1.5em"},onClick:B},{default:o(()=>[k("登录")]),_:1})]),_:1})]),_:1})):N("",!0),r.value==="手机号登录"?(u(),g(w,{key:1},{default:o(()=>[e(d,null,{default:o(()=>[e(i,{modelValue:_.userName,"onUpdate:modelValue":t[3]||(t[3]=s=>_.userName=s),placeholder:c.手机号码},null,8,["modelValue","placeholder"])]),_:1}),e(d,null,{default:o(()=>[e(i,{modelValue:_.password,"onUpdate:modelValue":t[4]||(t[4]=s=>_.password=s),type:"password",placeholder:c.密码},null,8,["modelValue","placeholder"]),W]),_:1})]),_:1})):N("",!0)])])])}}},oe=R(X,[["__scopeId","data-v-90ff4561"]]);export{oe as default};
