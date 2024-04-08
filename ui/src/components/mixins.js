
import axios from 'axios';
import Constants from '../constants.js'

export default {
  data() {
    return {};
  },
  computed: {
    publicPath() { return process.env.BASE_URL; },  // for static files linking
    offliner_flags() { return this.$store.getters.offliner_flags; }, // offliner flags for requests
  },
  methods: {
    toggleLoader(text) { // shortcut to store's loader status changer
      let payload = text ? {status: true, text: text} : {status: false};
      this.$store.dispatch('setLoading', payload);
    },
    redirectTo(name, params) {
      let route_entry = {name: name};
      if (params)
        route_entry.params = params;
      this.$router.push(route_entry);
    },
    alert(level, title, text, duration) {
      let message = "<strong>" + title + "</strong>";
      if (text)
        message += "<br />" + text;
      this.$root.$emit('feedback-message', level, message, duration);
    },
    alertInfo(title, text, duration) { this.alert('info', title, text, duration); },
    alertSuccess(title, text, duration) { this.alert('success', title, text, duration); },
    alertWarning(title, text, duration) { this.alert('warning', title, text, duration); },
    alertDanger(title, text, duration) { this.alert('danger', title, text, duration); },
    alertAccessRefused(perm_name) { this.alertWarning("Access Refused", "You don't have <code>" + perm_name + "</code> permission."); },
    alertError(text) { this.alertDanger("Error", text, Constants.ALERT_PERMANENT_DURATION); },

    statusClass(status) {
      if (status == 'succeeded')
        return 'schedule-suceedeed';
      if (["failed", "canceled", "cancel_requested"].indexOf(status))
        return 'schedule-failed';
      return 'schedule-running';
    },
    queryAPI(method, path_or_url, data, config) {
      console.debug("queryAPI", method, path_or_url);
      if (data === undefined)
        data = {};
      if (config === undefined)
        config = {};

      // returning straight request/promise
      return axios.create({
            // baseURL: Constants.zimfarm_webapi,
            headers: {},
            // paramsSerializer: Constants.params_serializer,
          })[method](path_or_url, data, config);
    },
  }
}
