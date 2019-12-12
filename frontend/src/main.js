import '@fortawesome/fontawesome-free/css/all.min.css';
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbvue/lib/css/mdb.min.css';
import Vue from 'vue';
import App from './App.vue';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import VueRouter from 'vue-router';
import list_of_teacherscards from './components/list_of_teachers_cards.vue'
import navbar from './components/navbar.vue'

Vue.use(VueRouter);
Vue.use(BootstrapVue);

Vue.config.productionTip = false;


const routes = [
  {
    path: '/teachers',
    name: 'teachers',
    component: list_of_teacherscards,
  },
  {
    path: '/',
    name: 'home',
    component: navbar
  }
];

const router = new VueRouter({
  routes,
  mode: 'history'
});

new Vue({
  el: '#app',
  router,
  render: h => h(App)
}).$mount('#app')
