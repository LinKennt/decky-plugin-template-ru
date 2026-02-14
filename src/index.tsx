import {
  ButtonItem,
  PanelSection,
  PanelSectionRow,
  Navigation,
  staticClasses
} from "@decky/ui";
import {
  addEventListener,
  removeEventListener,
  callable,
  definePlugin,
  toaster,
  // routerHook
} from "@decky/api"
import { useState } from "react";
import { FaShip } from "react-icons/fa";

// import logo from "../assets/logo.png";

// Эта функция вызывает python-функцию «add», которая принимает два числа и возвращает их сумму (в виде числа)
// Обратите внимание на аннотации типов:
// первый: [первый: номер, второй: номер] для аргументов
// второй: число для возвращаемого значения
const add = callable<[first: number, second: number], number>("add");

// Эта функция вызывает python-функцию "start_timer", которая не принимает аргументов и ничего не возвращает.
// Она запускает (python) таймер, который в конечном итоге генерирует событие 'timer_event'
const startTimer = callable<[], void>("start_timer");

function Content() {
  const [result, setResult] = useState<number | undefined>();

  const onClick = async () => {
    const result = await add(Math.random(), Math.random());
    setResult(result);
  };

  return (
    <PanelSection title="Секция панели">
      <PanelSectionRow>
        <ButtonItem
          layout="below"
          onClick={onClick}
        >
          {result ?? "Сложение двух чисел с помощью Python"}
        </ButtonItem>
      </PanelSectionRow>
      <PanelSectionRow>
        <ButtonItem
          layout="below"
          onClick={() => startTimer()}
        >
          {"Запуск Python таймера"}
        </ButtonItem>
      </PanelSectionRow>

      {/* <PanelSectionRow>
        <div style={{ display: "flex", justifyContent: "center" }}>
          <img src={logo} />
        </div>
      </PanelSectionRow> */}

      {/*<PanelSectionRow>
        <ButtonItem
          layout="below"
          onClick={() => {
            Navigation.Navigate("/decky-plugin-test");
            Navigation.CloseSideMenus();
          }}
        >
          Router
        </ButtonItem>
      </PanelSectionRow>*/}
    </PanelSection>
  );
};

export default definePlugin(() => {
  console.log("Инициализация шаблонного плагина, вызывается один раз при запуске интерфейса")

  // serverApi.routerHook.addRoute("/decky-plugin-test", DeckyPluginRouterTest, {
  //   exact: true,
  // });

  // Добавляем обработчик события для события "timer_event" из бэкенда
  const listener = addEventListener<[
    test1: string,
    test2: boolean,
    test3: number
  ]>("timer_event", (test1, test2, test3) => {
    console.log("Шаблон получил timer_event с:", test1, test2, test3)
    toaster.toast({
      title: "шаблон получил timer_event",
      body: `${test1}, ${test2}, ${test3}`
    });
  });

  return {
    // Имя, отображаемое в различных меню Decky
    name: "Тестовый плагин",
    // Элемент, отображаемый в верхней части меню вашего плагина.
    titleView: <div className={staticClasses.Title}>Пример плагина Decky</div>,
    // Содержимое меню вашего плагина
    content: <Content />,
    // Значок, отображаемый в списке плагинов
    icon: <FaShip />,
    // Функция, срабатывающая при выгрузке вашего плагина
    onDismount() {
      console.log("Unloading")
      removeEventListener("timer_event", listener);
      // serverApi.routerHook.removeRoute("/decky-plugin-test");
    },
  };
});
