# PRD — Plataforma de Gestão de Projetos Inspirada no OpenProject

## 1) Visão do produto
Construir uma plataforma web para planejamento, execução e acompanhamento de projetos, com colaboração integrada entre equipes e stakeholders.

**Proposta de valor**
- Centralizar trabalho, cronograma, comunicação e documentação em um único sistema.
- Melhorar previsibilidade de prazos e esforço.
- Aumentar transparência do progresso por time, projeto e portfólio.

## 2) Objetivos e resultados esperados
### Objetivos
1. Entregar um núcleo funcional de gestão de trabalho (work items + board + gantt).
2. Permitir governança de projetos com papéis e permissões por projeto.
3. Evoluir para visão executiva com relatórios, roadmap e portfólio.

### Indicadores (KPIs)
- % de tarefas concluídas no prazo.
- Lead time médio por tipo de item.
- Horas registradas vs. horas estimadas.
- Taxa de atualização semanal dos itens ativos.
- Nº de projetos com visibilidade executiva (portfólio ativo).

## 3) Escopo funcional

## 3.1 Módulo de identidade e acesso
- Login/logout.
- Recuperação de senha.
- Gestão de usuários (ativo/inativo).
- Papéis e permissões por projeto (RBAC).
- Associação de membros a projetos.

## 3.2 Módulo de projetos
- CRUD de projeto.
- Projeto pai/subprojeto.
- Arquivar/encerrar projeto.
- Template de projeto.
- Dashboard resumido por projeto.

## 3.3 Módulo de work items (núcleo)
- CRUD de item.
- Tipos: tarefa, bug, história, épico, risco, melhoria, incidente, marco.
- Campos: título, descrição, status, prioridade, responsável, datas, progresso, estimativa.
- Comentários e anexos.
- Seguidores/watchers.
- Subtarefas e hierarquia pai-filho.
- Relações (bloqueia, precede, depende de, relacionado a).
- Filtros, agrupamentos, ordenação e visualização tabular.

## 3.4 Módulo de Gantt e cronograma
- Timeline por item.
- Dependências predecessor/sucessor.
- Marcos.
- Edição por drag-and-drop.
- Filtros por período, status, responsável e projeto.
- Visão opcional multi-projeto.

## 3.5 Módulo ágil (boards)
- Board Kanban com colunas configuráveis.
- Cards arrastáveis.
- Filtros por sprint, responsável, etiqueta.
- Backlog e sprint.
- Swimlanes opcionais.
- Limites por coluna (WIP) no roadmap evolutivo.

## 3.6 Módulo de backlog, versão e roadmap
- Backlog priorizado (ranking manual).
- Planejamento por release/versão.
- Roadmap por período com entregas futuras.

## 3.7 Módulo de tempo e esforço
- Lançamento manual de horas.
- Temporizador start/stop por item.
- Edição de lançamentos.
- Relatórios por usuário, projeto, período e atividade.

## 3.8 Módulo de documentos
- Upload e categorização.
- Vínculo com projeto/item/reunião.
- Busca e permissões de acesso.
- Versionamento simples.

## 3.9 Módulo de reuniões
- Agenda/pauta.
- Participantes.
- Registro de atas, decisões e ações.
- Geração de ações vinculadas a work items.

## 3.10 Módulo de portfólio
- Visão consolidada multi-projeto.
- Saúde (semaforização), progresso e marcos críticos.
- Comparação entre projetos.

## 3.11 Módulo de notificações
- Eventos: atribuição, mudança de status, prazo próximo/vencido, comentário.
- Canais: in-app (MVP) e e-mail (fase posterior).

## 4) Requisitos funcionais (RF)
- **RF01** Gerenciar usuários, papéis e associações em projeto.
- **RF02** Criar, editar, arquivar e hierarquizar projetos.
- **RF03** Criar e manter work items com histórico, anexos e comentários.
- **RF04** Definir dependências e relações entre itens.
- **RF05** Exibir e editar cronograma em Gantt.
- **RF06** Operar board ágil com drag-and-drop.
- **RF07** Priorizar backlog e planejar sprint/release.
- **RF08** Registrar tempo manual e por temporizador.
- **RF09** Gerenciar documentos com busca e vínculo.
- **RF10** Gerenciar reuniões com ata e ações.
- **RF11** Gerar relatórios de progresso, esforço e atraso.
- **RF12** Notificar usuários por eventos relevantes.

## 5) Requisitos não funcionais (RNF)
- **RNF01** Interface web responsiva (desktop/mobile).
- **RNF02** RBAC por papel e por projeto.
- **RNF03** Auditoria e trilha de alterações.
- **RNF04** Performance em listas e boards com volume elevado.
- **RNF05** Arquitetura modular e escalável.
- **RNF06** API REST documentada.
- **RNF07** Segurança (hash de senha, proteção CSRF/XSS/SQLi, sessão segura).
- **RNF08** Acessibilidade (contraste, teclado, legibilidade).

## 6) Modelo conceitual de dados (alto nível)
Entidades:
- User, Role, Permission, Project, ProjectMember.
- WorkItem, WorkItemType, Status, Priority, Relation.
- Comment, Attachment.
- Board, BoardColumn, Sprint, Release.
- TimeEntry.
- Document.
- Meeting, MeetingAction.
- Portfolio.

Relações-chave:
- Projeto 1:N WorkItem.
- WorkItem 1:N subtarefas (self relation).
- WorkItem N:N WorkItem (Relation).
- User N:N Project (ProjectMember).
- WorkItem 1:N TimeEntry.
- Meeting 1:N MeetingAction, com vínculo opcional para WorkItem.

## 7) Regras de negócio
1. Usuário só acessa projetos em que é membro (exceto perfis administrativos).
2. Todo work item pertence a exatamente um projeto.
3. Dependências impactam datas e status de planejamento.
4. Registro de tempo deve ter usuário, item e data.
5. Board deve refletir status/critério configurado do projeto.
6. Transições de status dependem de papel e workflow.
7. Reuniões podem criar ações convertíveis em work items.
8. Módulos podem ser habilitados/desabilitados por projeto (ex.: tempo).

## 8) Priorização e roadmap de entrega
### Fase 1 (MVP)
- Identidade e acesso.
- Projetos e membros.
- Work items com comentários/anexos/relações básicas.
- Kanban básico.
- Gantt básico.
- Busca e filtros essenciais.

### Fase 2
- Time tracking completo.
- Backlog/sprint.
- Reuniões.
- Relatórios operacionais.
- Notificações in-app.

### Fase 3
- Portfólio.
- Roadmap/releases avançado.
- Automações.
- Integrações externas.
- Dashboards executivos.

## 9) Backlog inicial (épicos e histórias)
## Épico A — Identity & Access
- Como administrador, quero criar papéis para controlar permissões.
- Como gestor, quero convidar membros para meu projeto.

## Épico B — Projects
- Como gestor, quero criar projeto com template para acelerar setup.
- Como gestor, quero organizar subprojetos para refletir estrutura real.

## Épico C — Work Management
- Como membro, quero registrar comentários e anexos em uma tarefa.
- Como gestor, quero relacionar tarefas por dependência para planejar melhor.

## Épico D — Agile Boards
- Como equipe, quero mover cards entre colunas para atualizar o fluxo.
- Como PO, quero filtrar board por sprint/responsável.

## Épico E — Scheduling
- Como gestor, quero visualizar tarefas em Gantt com marcos.
- Como gestor, quero ajustar datas no gráfico para replanejar rapidamente.

## Épico F — Time & Effort
- Como membro, quero registrar horas por item.
- Como gestor, quero comparar horas estimadas vs. realizadas.

## Épico G — Meetings & Documents
- Como gestor, quero registrar ata e decisões da reunião.
- Como equipe, quero anexar e buscar documentos por projeto.

## Épico H — Portfolio & Reports
- Como diretor, quero ver saúde consolidada dos projetos.
- Como stakeholder, quero relatório de progresso por período.

## 10) Critérios de aceite (exemplos)
- Work item criado deve aparecer na lista e no board quando filtros permitirem.
- Alteração de status via board deve persistir e registrar histórico.
- Relação de dependência deve ser visível no Gantt.
- Lançamento de horas deve aparecer no relatório do período.
- Usuário sem permissão deve receber bloqueio de acesso a projeto.

## 11) Arquitetura sugerida para implementação
- **Frontend**: React + TypeScript.
- **Backend**: NestJS (Node.js).
- **Banco**: PostgreSQL.
- **ORM**: Prisma.
- **Auth**: JWT + refresh token.
- **Storage**: S3 compatível (ou filesystem no MVP).
- **API**: REST modular.

Módulos técnicos:
- core
- identity-access
- projects
- work-management
- agile-boards
- scheduling
- time-effort
- meetings
- documents
- portfolio
- reports
- notifications
- admin-settings

## 12) Fora de escopo inicial
- Billing/financeiro avançado.
- IA preditiva de prazo.
- Integrações profundas com ERP/CRM.
- Multi-tenant avançado com faturamento.

---

## Prompt operacional para Codex (implementação)
```text
Crie um sistema web modular de gestão de projetos inspirado em OpenProject.

Stack obrigatória:
- Frontend: React + TypeScript
- Backend: Node.js + NestJS
- Banco: PostgreSQL
- ORM: Prisma
- Autenticação: JWT com refresh token

Entregáveis obrigatórios:
1) Modelagem do banco com migrations
2) API REST documentada
3) Frontend completo do MVP Fase 1
4) Seeds de dados
5) README com setup local e execução
6) Coleção de exemplos de chamadas da API

Módulos MVP (fase 1):
- Identity & Access (RBAC por projeto)
- Projects
- Work Management (comentários, anexos, relações)
- Agile Boards (kanban básico com drag and drop)
- Scheduling (gantt básico com dependências)
- Busca/filtros essenciais

Requisitos técnicos:
- Arquitetura limpa e modular
- Código tipado e documentado
- Testes mínimos de API e domínio
- Logs e trilha de auditoria para alterações de status
```
