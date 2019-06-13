import './common';
//import './emsignpage';
//import Vue from 'vue';
//window.Vue = Vue;
import { VStepper } from 'vue-stepper-component'

export default {
  components: {
    VStepper
  },
  data: () => ({ steps: 3, step: undefined })
}
