import viteLogo from '/vite.svg'

/* ロゴ */
const Logo = (props) => (
    <img src={viteLogo} className="logo" alt="Vite logo" />
)

/* 基本レイアウト */
export default function Layout({ children }) {
    return (
        <div className="min-h-screen flex flex-col sm:justify-center items-center pt-6 sm:pt-0 bg-gray-100">
            <div>
                <a href="/">
                    <Logo className="w-20 h-20 fill-current text-gray-500" />
                </a>
            </div>
            {/* wrapper */}
            <div className="w-full sm:max-w-md mt-6 px-6 py-4 bg-white shadow-md overflow-hidden sm:rounded-lg">
                {children}
            </div>
        </div>
    );
}
