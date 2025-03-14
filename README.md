# Notes

Gabriel personal notes.
Created from [login-static-site](https://github.com/meadapt/login-static-site) repository.

## Usage

- Local server

```
git clone git@github.com:gabrielbdornas/notes.git
cd notes
poetry install
task serve
```

- Commit and push changes are enoth to guild and deploy the content to render.
This push will trigger the `publish_render_pages` GitHub Actions workflow that builds the site and pushes the generated static files to the render-pages branch.
