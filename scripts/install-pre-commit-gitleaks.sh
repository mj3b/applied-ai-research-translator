#!/usr/bin/env bash
set -euo pipefail

if ! command -v gitleaks >/dev/null 2>&1; then
  echo "gitleaks not found. Install it first (e.g., brew install gitleaks)."
  exit 1
fi

cat > .git/hooks/pre-commit <<'HOOK'
#!/usr/bin/env bash
set -euo pipefail
gitleaks protect --staged --redact --verbose --config .gitleaks.toml
HOOK

chmod +x .git/hooks/pre-commit
echo "Installed .git/hooks/pre-commit (gitleaks)"
