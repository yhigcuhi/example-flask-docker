// 基本ボタンs
export const Button = ({children, classNames = [''], disabled = false, ...props}) => {
    const _classNames = {
        'bg-green-800 text-white': disabled
    }

    return (
        <button
            className={[
                'bg-green-400 border border-gray-400 rounded-lg shadow-md px-4 py-2 text-sm font-mono text-gray-600'
                , ...Object.keys(_classNames).filter(k => _classNames[k])
                , ...classNames
            ].join(' ')}
            disabled={disabled}
            {...props}
        >
            {children}
        </button>
    );
}