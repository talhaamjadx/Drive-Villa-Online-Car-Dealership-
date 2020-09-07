import { csrftoken } from './csrf'
import axios from 'axios'

function apiService(url, method){
    var a= []
    if(method == 'GET'){
    axios({
        method: method,
        url: url,
        'X-CSRFTOKEN': csrftoken,
    })
    .then(res => {
        console.log(res)
        a= res.data
        console.log(a)
    })
    .catch(error => console.log(error))
    }
    return a
}

export { apiService }