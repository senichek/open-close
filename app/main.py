from fastapi import FastAPI, Depends, HTTPException
from app.services.payment_service import PaymentService, payment_service_registry

app = FastAPI()

def get_payment_service(payment_method_name: str) -> PaymentService:
    service_class = payment_service_registry.get(payment_method_name)
    if service_class is None:
        raise HTTPException(status_code=400, detail="Unsupported payment method")
    return service_class()


'''
Sample request:
curl --location --request POST 'http://127.0.0.1:8000/process-payment/?payment_method_name=credit_card' \
--data ''
'''
@app.post("/process-payment/")
def process_payment(payment_service: PaymentService = Depends(get_payment_service)):
    payment_service.process_payment()
    return {"message": f"Payment processed. {type(payment_service)}"}
