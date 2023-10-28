/* import react */
import {useRef, useState} from 'react';
/* import 部品 */
import {Button} from '../../components/index.jsx';
import viteLogo from '/vite.svg'
/* import hooks */
import {useFileUpload} from './hooks/useFileUpload.js'

/**
 * @returns {JSX.Element} ファイルアップロードフォーム画面
 */
export default function Form() {
    // input fileへの ref
    const fileRef = useRef();
    // 選択された ファイル名
    const [fileName, setFileName] = useState();
    // 選択された画像
    const [imageFile, setImageFile] = useState(viteLogo);
    // ファイルアップロード
    const {upload} = useFileUpload();

    /* イベントハンドラー*/
    // ファイルアップロードクリック
    const onClickUpload = () => fileRef.current.click()
    /**
     * ファイル変更
     * @param {React.ChangeEvent<HTMLInputElement>} event
     */
    const onChangeFile = async (event) => {
        // 設定されたファイル取得
        const files = event.currentTarget.files;
        // ファイルがなければ終了
        if (!files || files?.length === 0) return;
        // 先頭のファイルを取得
        const file = files[0];
        // ファイル名変更
        setFileName(file.name);
        // 選択 画像ファイル変更
        setImageFile(window.URL.createObjectURL(file));

        // ファイルアップロード
        const response = await upload(file)
        console.log('response...', response)
    }
    // 画面描画
    return (
        <div className='w-full flex flex-col gap-4'>
            {/* デバッグ用 画像ファイル名 */}
            <p className='text-lg'>{fileName ?? '画像を選択してください'}</p>
            {/* 選択した画像 表示 */}
            <img src={imageFile} className='max-w-sm text-center'/>
            {/* 画像選択 */}
            <Button
                onClick={onClickUpload}
                disabled={fileName}
            >
                {fileName ? 'Uploading...' : 'File upload'}
            </Button>
            {/* 画像選択のファイル入れる場所 */}
            <input
                ref={fileRef}
                type='file'
                accept='image/*'
                className='hidden'
                onChange={onChangeFile}
            />
        </div>
    )
}