# Đóng gói local hai pack 0.1.0

Hai thư mục là projection độc lập, không phải deployment hoặc release framework. Không dùng public-release-integration/gitlink, package registry, installer hoặc Actions. Đọc README bên trong từng pack để copy/cài; tệp này dành cho người bảo trì đóng asset.

## Kiểm tra trước đóng gói

Từ repository root, dùng Python và PyYAML đã có trong môi trường kiểm source. Không thay dependencies của runtime pack.

```powershell
python -B -m unittest discover -s distribution/tests -v
Push-Location 'Project Feather Core'
python -B -m unittest discover -s tests -p test_router_candidate.py
Pop-Location
python -B -m unittest discover -s 'Central Hub/tests'
git -c core.longpaths=true diff --check -- README.md distribution
```

FTH test dùng fixtures tạm. Nếu TEMP của môi trường không ghi được, đặt tempfile.tempdir tới workspace ghi được cho riêng process; không sửa source/tests để né sandbox.

## Tạo ZIP lặp lại

Chạy từ repository root. Truyền thư mục output tuyệt đối nằm ngoài tracked source; ví dụ workspace outputs. Không đưa ZIP vào distribution hoặc Git. Đoạn lệnh chỉ dùng standard library và từ chối ghi đè asset đã có. Chạy vào hai output directory mới để đối chiếu hash; không suy reproducibility chỉ vì code có fixed timestamp.

```powershell
@'
from pathlib import Path
import hashlib, sys, zipfile
out = Path(sys.argv[1]).resolve()
out.mkdir(parents=True, exist_ok=True)
for pack in ('FTH-Control-Pack', 'Central-Hub-Architecture-Pack'):
    root = Path('distribution') / pack
    target = out / (pack + '-v0.1.0.zip')
    if target.exists():
        raise SystemExit('Refuse overwrite: ' + str(target))
    with zipfile.ZipFile(target, 'x', compression=zipfile.ZIP_STORED) as archive:
        for path in sorted(root.rglob('*')):
            if path.is_symlink():
                raise SystemExit('Refuse symlink: ' + str(path))
            if path.is_file():
                info = zipfile.ZipInfo(pack + '/' + path.relative_to(root).as_posix(), (1980,1,1,0,0,0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                info.compress_type = zipfile.ZIP_STORED
                archive.writestr(info, path.read_bytes())
    print(target.name, hashlib.sha256(target.read_bytes()).hexdigest())
'@ | python -B - '<ABSOLUTE_OUTPUT_DIRECTORY>'
```

`distribution/.gitattributes` giữ nguyên byte vùng phân phối qua checkout, tránh core.autocrlf đổi YAML/LICENSE và làm lệch asset so với nội dung đã kiểm. File này chỉ phục vụ Git của repository nguồn, không nằm trong archive. ZIP_STORED tránh khác biệt do bộ nén; giữ nguyên byte UTF-8/line endings của pack, kể cả TECHNICAL/LICENSE sao byte-exact. Packaging không thay placeholder: asset là adaptation template cần cấu hình, không falsely configured deployment.

## Kiểm archive sau tạo và giải nén

```powershell
python -B distribution/tests/test_release_packs.py --archives '<ABSOLUTE_OUTPUT_DIRECTORY>'
```

Lệnh kiểm duplicate/unsafe paths, inventory allowlist, metadata, CRC, nội dung và giải nén vào TemporaryDirectory để so byte với pack đã kiểm. Tests bảo vệ tracked FTH/Hub bằng hashes baseline toàn subtree; khi source evolve về sau, failure đòi review provenance chứ không tự cho phép cập nhật baseline để làm xanh test.

## Phát hành về sau

Asset names: FTH-Control-Pack-v0.1.0.zip và Central-Hub-Architecture-Pack-v0.1.0.zip. Tag proposal tương ứng: fth-control-pack-v0.1.0 và central-hub-architecture-pack-v0.1.0. Chưa tạo tag, GitHub Release, push hoặc deploy; các thao tác đó cần authorization riêng. Mỗi archive chứa thư mục gốc riêng cùng README/LICENSE/notes/scenarios nên người tải không cần đọc repo history.

Phân biệt SOURCE-DERIVED, STATICALLY VERIFIED, REGRESSION VERIFIED (configuration fixture/source-preservation), PACKAGING VERIFIED và LIVE VERIFIED. Quy trình đóng ZIP không tạo live evidence.
