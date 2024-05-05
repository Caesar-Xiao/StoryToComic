import axiosRequest from "./Axios";

export default function loadTextFile(url: string, callback?: Function) {
    axiosRequest.post(`/${url}`)
        .then((res) => {
            if (callback)
                callback(res);
        }).catch((err) => {
            if (callback)
                callback(`故事读取失败！\n${err}`);
        });
}