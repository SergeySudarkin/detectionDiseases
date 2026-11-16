import cls from "./Header.module.css";
import { useNavigate } from "react-router-dom";
import ReactLogo from "../../assets/react.svg";
import { Button } from "../Button/Button";

export const Header = () => {
    const navigate = useNavigate();

    return (
        <header className={cls.header}>
            <div className={`${cls.wrapper} container`}>
                <p onClick={() => navigate("/")}>
                    <img src={ReactLogo} alt="react logo" />
                    <span>Detection Diseases</span>
                </p>
                <nav className={cls.menu}>
                    <ul className={cls.menuList}>
                        <li className={cls.menuItem}>
                            <a href="#" onClick={() => navigate("/")}>Пункт 1</a>
                        </li>
                        <li className={cls.menuItem}>
                            <a href="#" onClick={() => navigate("/")}>Пункт 2</a>
                        </li>
                        <li className={cls.menuItem}>
                            <a href="#" onClick={() => navigate("/")}>Пункт 3</a>
                        </li >
                    </ul >
                </nav >
                <div className={cls.headerButtons}>
                    <Button isActive onClick={""}>Войти</Button>
                    <Button isActive onClick={""}>Зарегистрироваться</Button>
                </div>
            </div>
        </header >
    );
};
