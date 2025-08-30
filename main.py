from dotenv import load_dotenv

# Muhit o‘zgaruvchilarini yuklash (.env fayldan)
load_dotenv()


def main():
    from graph_builder import build_graph

    # Graph yaratish
    graph = build_graph()

    # Foydalanuvchi topshirig‘ini olish
    task = input("AI agent uchun Python vazifasini kiriting: ")

    # Boshlang‘ich holat
    initial_state = {
        "task": task,        # vazifa matni
        "code": "",          # Writer yozadigan kod
        "explanation": "",   # Kod izohi
        "result": "",        # Tester natijasi (PASS/FAIL/ERROR)
        "details": "",       # Tester batafsil javobi
        "retries": 0         # Qayta urinishlar soni
    }

    final_state = None

    # Graph oqimini ishga tushirish
    for event in graph.stream(initial_state, stream_mode="updates"):
        for node, update in event.items():
            final_state = {**(final_state or initial_state), **update}

            # Oraliq natijani ham chiqarish mumkin
            print(f"\n[{node.upper()} bosqichi natijasi]")
            for k, v in update.items():
                print(f"  {k}: {v}")

    # Yakuniy natija
    if final_state:
        print("\n=== Yakuniy Holat ===")
        for key, value in final_state.items():
            print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
