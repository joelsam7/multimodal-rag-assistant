from app.services.qwen_service import qwen_service

answer = qwen_service.generate_response("Say hello in one sentence.")

print(answer)