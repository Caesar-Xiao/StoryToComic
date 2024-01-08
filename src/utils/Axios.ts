import axios from 'axios';

//使用create方法创建axios实例
const axiosRequst = axios.create({
    baseURL: '/api',
    headers: {
        'Content-Type': 'application/json;charset=UTF-8'
    }
});

// 添加请求拦截器
axiosRequst.interceptors.request.use(
    config => config,
    error => Promise.reject(error)
);

// 添加响应拦截器
axiosRequst.interceptors.response.use(
    response => response.data,
    error => Promise.reject(error)
);

export default axiosRequst;