import axiosRequest from "./Axios";

export default function callPython(script: string, prompt: string, callback?: Function) {
    axiosRequest.get("/call-python", {
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