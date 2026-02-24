#!/bin/bash

set -euo pipefail

TARGET_DIR="by_step_matrices"

if [[ "${1:-}" == "--random" ]]; then
  TARGET_DIR="random_matrices"
fi

if [ -d "$TARGET_DIR" ]; then
  rm -rf -- "$TARGET_DIR"/*
  echo "Все файлы из папки $TARGET_DIR удалены."
else
  echo "Ошибка: Папка $TARGET_DIR не существует."
fi