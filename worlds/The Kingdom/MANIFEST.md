# The Kingdom — Package Manifest v1.0

Status: ACTIVE
Version: 1.0
Role: PACKAGE_INTEGRITY

## Admission có phạm vi

Danh sách dưới đây nhận tệp vào package cho nhiệm vụ quản lý, không là cấp canon. Thêm owner có material bằng scoped author decision/review, rồi header và admission; validator --write chỉ làm mới vùng generated, không tự admit hoặc tạo owner. SOURCE_ID giữ ổn định khi rename. Control families và dependency do Router khai báo; highest ACTIVE numeric version được kiểm compatibility trước runtime. Không dependency global/FTH ở runtime.

<!-- BEGIN PACKAGE CONTRACT -->
```json
{
  "version": "1.0",
  "status": "ACTIVE",
  "sources": [
    "TK_DOMAIN_COUNTERINTELLIGENCE.md",
    "TK_DOMAIN_GEOPOLITICS.md",
    "TK_DOMAIN_HEALTH.md",
    "TK_DOMAIN_INFRASTRUCTURE.md",
    "TK_DOMAIN_LANGUAGE_RELIGION.md",
    "TK_DOMAIN_LAW.md",
    "TK_DOMAIN_OPENING_DELEGATION.md",
    "TK_DOMAIN_POT.md",
    "TK_METHOD_FICTION.md",
    "TK_METHOD_POV_PERSPECTIVE.md",
    "TK_TIMELINE_CP01_OPENING.md",
    "TK_TIMELINE_CP02_REVEAL.md",
    "TK_TIMELINE_INTERVAL_CP01_CP02.md",
    "TK_TIMELINE_POST_CP02.md"
  ],
  "navigation": [
    "README.md",
    "TK_CURRENT_SOURCE_INDEX.md",
    "THE_KINGDOM_CHECKPOINT_STATE_INDEX.md"
  ],
  "records": [
    "TK_RECONCILIATION_RECORD.md",
    "TK_OPEN_ISSUES_CURRENT.md"
  ],
  "support_controls": [
    "controls/multi_paracosm_hub_workflow.md",
    "controls/TK_WORLDBUILDING_STRESS_TEST.md"
  ],
  "maintenance": [
    "tools/validate_kingdom_package.py",
    "tests/test_kingdom_package.py",
    "tests/control_cases.json"
  ]
}
```
<!-- END PACKAGE CONTRACT -->

## Bảo trì

`python -B tools/validate_kingdom_package.py --check` là mặc định chỉ đọc. `--write` chỉ thay vùng GENERATED SOURCE CATALOG ở index và GENERATED HASHES ở manifest sau khi cấu trúc hợp lệ; không ghi lore, tự sửa source, di chuyển file, infer canon/dependency hoặc promote archive. Check stale phải báo rõ; scoped write theo yêu cầu bảo trì rồi check lại. Các input thay đổi giữa lúc tính/ghi phải chặn; hai lần thay tệp không là giao dịch chống mất điện, check tiếp phát hiện bản dở.

`Source_archive/` không tham gia current discovery, hash refresh, source load hoặc build/regeneration. Link provenance không là build dependency. Rollback dùng Git history. Thuộc tính read-only không là semantic authority. Manifest không tự hash chính nó; contract được parser/validation kiểm, các file current còn lại có hash bên dưới.

PyYAML cần cho đọc Router; môi trường task có sẵn 6.0.3. Không thêm model runner, không có semantic PASS hoặc live deployment từ phép kiểm này.

<!-- BEGIN GENERATED HASHES -->
| File | SHA-256 |
| --- | --- |
| `README.md` | `2cf9663fdb2e2d8f42ca70641efa4116f2397d6b31b38aa385b7c385948c7340` |
| `THE_KINGDOM_CHECKPOINT_STATE_INDEX.md` | `715a884670eec3611a5d16a450a01ec8768315cf76d4a0e7bd24145533a0d337` |
| `TK_CURRENT_SOURCE_INDEX.md` | `843c2f5af80d8f840309463c3e3f3e9452b4123c68af42d80fdd43db7f2279a0` |
| `TK_DOMAIN_COUNTERINTELLIGENCE.md` | `35b2069b3e43c09b57c94b8c00304ce62670f0fa7b813cf7a3493c506677e932` |
| `TK_DOMAIN_GEOPOLITICS.md` | `5710db1c95ed948b6d416dcda9281c75b3c2830be6d38e894a22e2562adbb22b` |
| `TK_DOMAIN_HEALTH.md` | `072a9ea40bd6085e855d382f62c59f7ce9ae0b1916c3a5eec7ae9db1a5cee304` |
| `TK_DOMAIN_INFRASTRUCTURE.md` | `379973086642f2cb75ebd480a540c17379d07ade1e853957ae1cd94045629cf3` |
| `TK_DOMAIN_LANGUAGE_RELIGION.md` | `66597f79ef81e33ba2268e6a705970870ac29c45db0d9129c01dd3f066f625c3` |
| `TK_DOMAIN_LAW.md` | `1d2a235b4b45b89a3613a511e44dac00c707f123a7a765e01b0030aae08506ee` |
| `TK_DOMAIN_OPENING_DELEGATION.md` | `69bd357e2489814440d5690175b237d4c7077e83cd10b785a1e2e7ed2a2c589e` |
| `TK_DOMAIN_POT.md` | `b491a5ae4200d489682ebc9e21c6d5e6db66f1c1854400d4441f01b52de8c483` |
| `TK_METHOD_FICTION.md` | `940719d43448ac0d5bb6c9dfae340e1762510a91e32fee2de7beeb37f5f2b5ca` |
| `TK_METHOD_POV_PERSPECTIVE.md` | `6dc0d065f8fac14f047bef508990d72e859132063ad4c4d0551584f430333790` |
| `TK_OPEN_ISSUES_CURRENT.md` | `a5b8fcdbc3c5ff76e00e9616f69bffb35412ff49f5d665ffe72578fd22b8a7b4` |
| `TK_RECONCILIATION_RECORD.md` | `d734a85cd5f93f30ccb8050db110230a79d8750c634f5d9c5a96bc9668f59e7b` |
| `TK_TIMELINE_CP01_OPENING.md` | `246b547c585f69d2fcffde58721444cc28a068218582031a857e20948b8a5118` |
| `TK_TIMELINE_CP02_REVEAL.md` | `57b1bf66dc8f8c993d29a568dd0e87fc96863dc378c4132b10734730fccd97da` |
| `TK_TIMELINE_INTERVAL_CP01_CP02.md` | `f01b50124a6173afe66b795697d63a5c734c7b39be9efa8119a1613c7bd877ea` |
| `TK_TIMELINE_POST_CP02.md` | `016f21b38470d756c3f1b2ff68da3b7a644fb98eb8b406fb0093104bdbf30a5e` |
| `controls/TK_AUTHORING_PIPELINE_v1.0.md` | `de9d830bc9114120de580442dbdb27fe9316ff08c0bd8f358711d93c242544df` |
| `controls/TK_CI_v1.0.md` | `510556a353a8933ff02e8f6e7d56650503f64703239ac60ef465c558da5d1343` |
| `controls/TK_CONTROL_VOCABULARY_GLOSSARY_v1.0.md` | `612509334868231ed2202077c1f236b84270b4d62d4b9fa4f39fc9c993215cff` |
| `controls/TK_ROUTER_v1.0.yaml` | `dde08b249c9955084f04dbf71c3968c41082eb926d5b890a946d939b9ec066cb` |
| `controls/TK_WORLDBUILDING_STRESS_TEST.md` | `ad5f7dc02fbe0f36edab209249d79aaa0eb5b7bd9c2b553d0f8a9a642dd7dc10` |
| `controls/anti_drift/TK_Anti_Drift_Actor_Knowledge_Reception_Model_Update_v1.0.md` | `bb43cb6732305f03004b5feac2d4cec969998515bd3c82b624f4fcc7bbe20886` |
| `controls/anti_drift/TK_Anti_Drift_Belief_Culture_Divinity_v1.0.md` | `0ccb0a1efec17d41dbdd0196016b392c09f2bf740f068169b89e24312641922e` |
| `controls/anti_drift/TK_Anti_Drift_Economy_Trade_Abundance_v1.0.md` | `4b8e1c432e927eb585ad286629cd2b1f96b321924a9ce714ee320a6afb05f854` |
| `controls/anti_drift/TK_Anti_Drift_IRL_Baseline_Divergence_v1.0.md` | `78381d73c402861b74c0bdc633368edd169151a33055c69cee22bf757d712b60` |
| `controls/anti_drift/TK_Anti_Drift_State_Relation_Architecture_v1.0.md` | `29c4714b4ad35f17673e4e538efb9b6748a505d301504b618c61619df525906d` |
| `controls/anti_drift/TK_Anti_Drift_Strategic_Crisis_Conflict_v1.0.md` | `4e5a2bd02e117b1c4402e8a6937e86b6610bbb63c1ea9cfc9f320c4ca8dfbade` |
| `controls/anti_drift/TK_Anti_Drift_Temporal_World_State_v1.0.md` | `30d7dc1bea44281c961d5000a6637b6c760c2acb3530ca498c50f66aade7b799` |
| `controls/anti_drift/TK_Anti_Drift_World_Institutional_Logic_v1.0.md` | `75de2c0da7d0547b5ea13feec788ee264a7192ae7908c1a8e578263c5df204ee` |
| `controls/anti_drift/TK_Anti_Drift_World_State_Narrative_Assumption_Failure_v1.0.md` | `7f9113e797e66e0f35ff2914d86769364d2d1e04bc1f7fa19448aa0d2ff3f280` |
| `controls/multi_paracosm_hub_workflow.md` | `2d401ad6a0981062f60de21d85531905fc09c88c58f66ec2170268c48c492430` |
| `tests/control_cases.json` | `c3e7c7d44e890e423b20aeaede27bcb541727e5b69661822ea0846af97a63983` |
| `tests/test_kingdom_package.py` | `a8c845ec1aab6e3e047f647755d1374d9020ad2dade40a83fe10b88360dc6dae` |
| `tools/validate_kingdom_package.py` | `79bdc48fe7bb652030c9fd6abacb740896b45ff965087c67157edfbec62b59bd` |

<!-- END GENERATED HASHES -->
