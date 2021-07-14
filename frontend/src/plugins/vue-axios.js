import { CSRF_TOKEN } from "../common/csrf_token.js";

const VueAxiosPlugin = {}
export default VueAxiosPlugin.install = function (Vue, { axios }) {
    axios.defaults.headers.common = {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFTOKEN": CSRF_TOKEN
    }

    Vue.axios = axios
    Object.defineProperties(Vue.prototype, {
        axios: {
            get() {
                return axios
            }
        }
    })
}