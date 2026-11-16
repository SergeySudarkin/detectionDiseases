import { Outlet } from "react-router-dom";
import cls from "./MainLayout.module.css";
import { Header } from "../Header/Header";

export const MainLayout = () => {
    const currentYear = new Date().getFullYear();

    return (
        <>
            <div className={cls.mainLayout}>
                <Header />
                <div className={cls.mainWrapper}>
                    <main className={cls.main}>
                        <div className="container">
                            <Outlet />
                        </div>
                    </main>
                    <footer className={cls.footer}>
                        <div className="container">
                            <p>
                                Cайт для пациентов по раннему выявлению ревматологических заболеваний | {currentYear}
                            </p>
                        </div>
                    </footer>
                </div>
            </div>
        </>
    );
};
