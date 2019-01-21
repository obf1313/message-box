import axios from 'axios'

let Ajax = {
    post: (url, data)=> {
        return axios({ method: 'post', url, data, baseURL: '/api'}).then(function(response) {
            return response.data
        }).catch((error)=>{
            window.console.log(error)
        })
    },
    get: (url, data)=> {
        return axios.get('http://127.0.0.1:8000'+url, data).then(function(response) {
            return response.data
        }).catch((error)=>{
            window.console.log(error)
        })
    }
}
export default Ajax;
