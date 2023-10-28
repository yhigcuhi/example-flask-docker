/* import api */
import {upload as uploadAPI} from '@/api/upload.js'

/**
 * ファイルアップロード hooks
 */
export const useFileUpload = () => {
    /**
     * ファイルアップロード
     * @param {File} file
     * @return {Promise<void>} API結果
     */
    const upload = async (file) => {
        // 前提条件
        if (!file) return // 未選択
        // ファイルアップロードAPI実行
        return uploadAPI(file)
    }

    // export
    return {
        upload
    }
}