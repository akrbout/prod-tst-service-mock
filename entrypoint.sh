#!/bin/sh
set -e

if [ "$APP_TYPE" = "cian" ]; then
  echo "Will run cian_mock_service application"
  exec uv run uvicorn cian_mock_service.main:app --host 0.0.0.0 --port 80
elif [ "$APP_TYPE" = "hh" ]; then
  echo "Will run hh_mock_service application"
  exec uv run uvicorn hh_mock_service.main:app --host 0.0.0.0 --port 80
elif [ "$APP_TYPE" = "tk" ]; then
  echo "Will run tk_mock_service application"
  exec uv run uvicorn tk_mock_service.main:app --host 0.0.0.0 --port 80
else
  echo "Will run nothing, unknown app type - $APP_TYPE"
fi