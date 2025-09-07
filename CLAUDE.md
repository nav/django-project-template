# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Environment Setup
- `make install` - Install dependencies, run Docker services, create superuser and tenant
- `make run/docker` - Start Docker services (PostgreSQL, Redis, MinIO)
- `uv sync` - Install Python dependencies

### Running the Application  
- `make run` - Run Django with Gunicorn (production-like)
- `make server` - Run Django development server on 0.0.0.0:8000
- `uv run python src/manage.py runserver 0.0.0.0:8000` - Alternative dev server command

### Testing
- `make test` - Run all tests with pytest
- `make test path=src/app/tests/test_models.py` - Run specific test file
- `uv run pytest src/app/tests/test_models.py::TestClassName::test_method` - Run specific test

### Code Quality
- `uv run ruff check` - Run linter (configured in pyproject.toml)
- `uv run ruff format` - Auto-format code
- `uv run pyright` - Type checking
- `uv run black src/` - Format code (alternative to ruff format)

### Database Management
- `make migrate` - Run Django migrations
- `make migrations` - Create new Django migrations
- `make db` - Recreate database (with credentials setup)
- `uv run python src/manage.py createtenant` - Create new tenant

### Static Files & Assets
- `make static` - Collect static files for production
- `make css` - Watch and compile Tailwind CSS

## Project Architecture

### Multi-Tenant Django Application
This is a Django template for multi-tenant SaaS applications with these key architectural patterns:

**Core Apps Structure:**
- `src/project/` - Django project configuration, main URLs, middleware
- `src/tenant/` - Multi-tenancy logic, User model, tenant management
- `src/infrastructure/` - Shared utilities, base models, custom fields
- `src/integration/` - External service integrations and configuration storage

**Multi-Tenancy Pattern:**
- Each tenant has a unique subdomain mapped via Django Sites framework
- `Tenant` model linked to Django's `Site` model for domain-based routing
- `Tenanted` abstract base class for tenant-scoped models
- Custom `User` model inherits from `AbstractUser` with ULID primary keys
- Membership system for user-tenant-group relationships

**Base Model Patterns:**
- `Audited` - Automatic created_at/updated_at timestamps
- `Deactivatable` - Soft deletion with is_active field and custom manager
- `Tenanted` - Automatic tenant association for multi-tenant models
- `UlidField` - Custom field for ULID identifiers with prefixes (e.g., "usr_", "tnt_")

**Key Technologies:**
- Django 5.1+ with PostgreSQL primary database
- Redis for caching and sessions
- MinIO/S3 for file storage via django-storages
- WhiteNoise for static file serving
- django-allauth for authentication (social login ready)
- Tailwind CSS for styling
- pytest-django for testing with factory-boy fixtures
- Gunicorn for WSGI serving
- Prometheus metrics integration

### Custom Middleware & Features
- `LoginRequiredMiddleware` - Global login requirement with URL exemptions
- Prometheus metrics collection at `/metrics`
- Sentry error tracking (production only)
- Custom context processors in `infrastructure.context_processors`

### Configuration Management
- Settings use environment variables with sensible defaults
- `.pgpass` file for PostgreSQL authentication
- Development vs production configuration via `DEBUG` environment variable
- Docker Compose for local development services

### Testing Strategy
- pytest with Django integration
- Factory Boy for test data creation
- Separate test database configuration
- Coverage reporting configured but commented out
- Tests organized in `src/*/tests/` directories

### File Organization
- Source code in `src/` directory
- Templates in `src/templates/`
- Static files in `src/static/`
- Each app follows Django conventions with models, views, admin, etc.
- Migration folders are tracked in git (empty __init__.py files)

When working with this codebase, always consider the multi-tenant nature and ensure new models either inherit from `Tenanted` (if tenant-specific) or remain global. Use the existing ULID field pattern for new models and follow the established soft-deletion patterns with `Deactivatable`.
