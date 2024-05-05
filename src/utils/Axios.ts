import axios from 'axios';

//使用create方法创建axios实例
const axiosRequest = axios.create({
    baseURL: '/api',
    headers: {
        'Content-Type': 'application/json;charset=UTF-8'
    }
});

// 添加请求拦截器
axiosRequest.interceptors.request.use(
    config => config,
    error => Promise.reject(error)
);

// 添加响应拦截器
axiosRequest.interceptors.response.use(
    response => response.data,
    error => Promise.reject(error)
);

export default axiosRequest;