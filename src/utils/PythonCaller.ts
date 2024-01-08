import axiosRequst from "./Axios";

export default function callPthon(script: string, prompt: string, callback?: Function) {
    axiosRequst.get("/call-python", {
        params: {
            script: script,
            prompt: prompt
        }
    }).then((res) => {
        if (callback)
            callback(res);
    }).catch((err) => {
        if (callback)
            callback(err);
    });
}