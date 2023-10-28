/* import axios */
import Axios from 'axios'

/* 内部参照可能定数 */
const BASE_URL = 'http://localhost:8080/api' // TODO:vite envで表現

// api用の axios インスタンス生成
const myAxios = Axios.create({
    baseURL: `${BASE_URL}`,
})
// export
export default myAxios;
