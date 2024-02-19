import axiosRequst from "./Axios";

export default function loadTextFile(url: string, callback?: Function) {
    axiosRequst.post(`/${url}`)
        .then((res) => {
            if (callback)
                callback(res);
        }).catch((err) => {
            if (callback)
                callback(`故事读取失败！\n${err}`);
        });
}