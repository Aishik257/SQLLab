let editor;

require.config({
    paths: {
        vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }
});

require(["vs/editor/editor.main"], function () {

    monaco.editor.defineTheme("sqllab-dark", {
        base: "vs-dark",
        inherit: true,
        rules: [
            {
                token: "keyword",
                foreground: "569CD6"
            },
            {
                token: "string",
                foreground: "CE9178"
            },
            {
                token: "number",
                foreground: "B5CEA8"
            }
        ],
        colors: {
            "editor.background": "#0d1117",
            "editorLineNumber.foreground": "#6e7681",
            "editorCursor.foreground": "#f0f6fc",
            "editor.selectionBackground": "#264f78",
            "editor.lineHighlightBackground": "#161b22",
            "editorIndentGuide.background": "#30363d",
            "editorIndentGuide.activeBackground": "#484f58"
        }
    });

    const editorContainer =
        document.getElementById("editor");

    const hiddenInput =
        document.getElementById("query-input");

    let initialQuery =
        window.initialQuery || "";

    if (!initialQuery) {

        initialQuery = `SELECT *
FROM sqlite_master;`;

    }

    editor = monaco.editor.create(
        editorContainer,
        {
            value: initialQuery,

            language: "sql",

            theme: "sqllab-dark",

            automaticLayout: true,

            minimap: {
                enabled: false
            },

            fontFamily:
                "JetBrains Mono",

            fontSize: 14,

            fontLigatures: true,

            lineNumbers: "on",

            roundedSelection: false,

            scrollBeyondLastLine: false,

            wordWrap: "on",

            tabSize: 4,

            insertSpaces: true,

            cursorBlinking: "smooth",

            smoothScrolling: true,

            padding: {
                top: 20,
                bottom: 20
            }
        }
    );

    hiddenInput.value =
        editor.getValue();

    editor.onDidChangeModelContent(
        function () {

            hiddenInput.value =
                editor.getValue();

        }
    );

    editor.addCommand(
        monaco.KeyMod.CtrlCmd |
        monaco.KeyCode.Enter,
        function () {

            document
                .getElementById("query-form")
                .submit();

        }
    );

    editor.focus();
});

document.addEventListener(
    "DOMContentLoaded",
    function () {

        const form =
            document.getElementById("query-form");

        if (!form) return;

        form.addEventListener(
            "submit",
            function () {

                const hiddenInput =
                    document.getElementById(
                        "query-input"
                    );

                if (
                    editor &&
                    hiddenInput
                ) {

                    hiddenInput.value =
                        editor.getValue();

                }

            }
        );
    }
);