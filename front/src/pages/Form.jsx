/* import react */
import {useRef, useState} from 'react';
/* import 部品 */
import {Button} from '../components';
import viteLogo from '/vite.svg'

export default function Form() {
    // input fileへの ref
    const fileRef = useRef();
    // アップロードする ファイル名
    const [fileName, setFileName] = useState();
    // アップロードする画像
    const [imageFile, setImageFile] = useState(viteLogo);

    /* イベントハンドラー*/
    // ファイルアップロードクリック
    const onClickUpload = () => fileRef.current.click()
    /**
     * ファイル変更
     * @param {React.ChangeEvent<HTMLInputElement>} event
     */
    const onChangeFile = (event) => {
        // 設定されたファイル取得
        const files = event.currentTarget.files;
        // ファイルがなければ終了
        if (!files || files?.length === 0) return;
        // 先頭のファイルを取得
        const file = files[0];
        // ファイル名変更
        setFileName(file.name);
        // 画像ファイル変更
        setImageFile(window.URL.createObjectURL(file));

        // TODO:次 flaskへファイルアップロード...
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