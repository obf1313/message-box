import axios from 'axios'
import { Message } from 'element-ui'

let Ajax = {
    post: (url, data)=> {
        return axios({ method: 'post', url, data, baseURL: '/api'}).then(function(response) {
            return response.data
        }).catch((error)=>{
            if(error.response) {
                if(error.response.status === '404'){
                    Message.error('服务未找到！');
                }else if(error.response.status === '500'){
                    Message.error('服务器异常！');
                }else{
                    Message.error('未知异常！');
                }
            }
        })
    },
    get: (url, data)=> {
        return axios({ method: 'get', url, data, baseURL: '/api'}).then(function(response) {
            return response.data
        }).catch((error)=>{
            if(error.response) {
                if(error.response.status === '404'){
                    Message.error('服务未找到！');
                }else if(error.response.status === '500'){
                    Message.error('服务器异常！');
                }else{
                    Message.error('未知异常！');
                }
            }
        })
    }
}
export default Ajax;
