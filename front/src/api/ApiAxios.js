/* import axios */
import Axios from 'axios'

/* 内部参照可能定数 */
const BASE_URL = 'http://localhost:8080/api' // TODO:vite envで表現
const API_KEY = import.meta.env.VITE_API_KEY

// api用の axios インスタンス生成
const myAxios = Axios.create({
    baseURL: `${BASE_URL}`,
    headers: {
        'X-API-KEY': API_KEY // API 利用キー
    }
})
// export
export default myAxios;
