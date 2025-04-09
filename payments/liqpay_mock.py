import random

class MockLiqPay:
    @staticmethod
    def create_payment(user_id: int, amount: float) -> str:
        # Симулюємо створення платіжного посилання
        return f"https://mock.liqpay.ua/payment?uid={user_id}&amount={amount}"

    @staticmethod
    def check_payment_status() -> str:
        return random.choice(["success", "fail"])
