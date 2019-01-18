import axios from 'axios'

let Ajax = {
    post: function (url, data={}) {
        return axios.post('http://127.0.0.1:8000/messageBox'+url, JSON.stringify(data)).then(function(response) {
            window.console.log(response)
        }).catch((error)=>{
            window.console.log(error)
        })
    },
    get: function (url, data={}) {
        return axios.get('http://127.0.0.1:8000/messageBox'+url, data).then(function(response) {
            window.console.log(response)
        }).catch((error)=>{
            window.console.log(error)
        })
    }
}
export default Ajax;
