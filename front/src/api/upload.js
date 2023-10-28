/* import axios */
import axios from './ApiAxios'
// ルーティング
const ROUTES = {
    upload: '/v1/upload'
}

/**
 * ファイルアップロード
 * @param {File} file アップロードファイル
 * @return {Promise<axios.AxiosResponse<any>>} API結果s
 */
export const upload = (file) => {
    // アップロード リクエストボディ = multipart/form-data
    const formData = new FormData()
    formData.append('image', file) // name="image"

    // multipart/form-dataでリクエスト
    return axios.post(ROUTES.upload, formData, {
        headers: {
            'content-type': 'multipart/form-data',
            // TODO:X-API-KEYへの対応、CORSへの対応をサーバー側
        }
    })
}