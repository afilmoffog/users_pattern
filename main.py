import uvicorn
import os

if __name__ == '__main__':
    uvicorn.run('app:app', host="0.0.0.0", port=int(os.environ.get('PORT', 3000)), reload=True)
