# zBricks 0.0.1

Rapid application framework, built on `Flask`.

### Features

#### zBrick class /  `Attachable` / `AttachmentHost`
- [x] `AttachmentHost.attach(child:Attachable)` -> `child._attach_to(parent:AttachmentHost)`
- [ ] Type-checking of both `AttachmentHost` and `Attachable` for compatability

#### Themes and Templates
Provided by `zbricks.themes.DefaultTheme`
- [x] Injects default templating, making use of Bootstrap / Bootswatch CDN
- [ ] `zbricks.themes.BaseTheme`
- [ ] Passing config data during init
- [ ] Context Preprocessor to inject config data into rendering process
- [ ] Once the above is done: Themes able to be set/configured _per user_

#### SQLAlchemy and Models
Provided by `zbricks.sqla.SQLAlchemyStorage`
- [ ] `zbricks.sqla.Base` and `SQLAlchemy(model_base=zbricks.sqla.Base)`
- [ ] `Storage` protocol
- [ ] ...

#### Authentication Service
Provided by `zbricks.auth.AuthenticationService`
- [ ] Use callbacks to check data e.g. `auth = AuthenticationService(user_by_id_callback = storage.get_user_by_id)`
- [ ] `@zbricks.auth.requires_user()`
- [ ] `@zbricks.auth.requires_permission('foo')`, 
- [ ] `@zbricks.auth.requires_role('admin')`, 