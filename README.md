# 1c-team

Плагин Claude Code: команда агентов для разработки на 1С. Работает поверх плагина `unica`.

## Состав
- Агенты: `analyst`, `architect`, `developer`, `query-writer`, `reviewer`.
- Команды: `/1c-team:spec`, `/1c-team:task`, `/1c-team:quick`.
- Скилл: `spec-template` — шаблон спецификации.

## Установка
```
claude plugin marketplace add <владелец>/<репозиторий>
claude plugin install 1c-team@ivan-1c
```

## Обновление
Поднять `version` в `plugins/1c-team/.claude-plugin/plugin.json`, закоммитить, затем:
```
claude plugin marketplace update ivan-1c
claude plugin update 1c-team@ivan-1c
```

## Благодарности
Идеи ролей и процесса навеяны:
- [rmartynenko/workflow-dev-1c-claude-code](https://github.com/rmartynenko/workflow-dev-1c-claude-code) (MIT)
- [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) (MIT)

Тексты агентов, команд и шаблона написаны заново.

## Лицензия
MIT — см. [LICENSE](LICENSE).
