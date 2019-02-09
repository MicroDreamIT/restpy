
require('./bootstrap');

window.Vue = require('vue');
import Vue from 'vue'
Vue.component('example-component', require('./components/ExampleComponent.vue').default);

const app = new Vue({
    el: '#app',
    delimiters: ['{', '}'],

    data:{
        message:'Hi this is testing',
        drawer: null,
    }
});
