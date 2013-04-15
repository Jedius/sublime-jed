from os.path import splitext, basename, dirname, join
import sublime_plugin


class AutoBuild(sublime_plugin.EventListener):
    def on_post_save(self, view):
        file_path = view.file_name()
        working_dir = dirname(file_path)
        file_name, file_type = splitext(basename(file_path))
        redir = False

        if file_type == '.coffee':
            cmd = ["/usr/local/bin/coffee", "-c", file_path]

        elif file_type == '.less':
            output_file = join(working_dir, file_name + '.css')
            cmd = ["/usr/local/lib/node_modules/less/bin/lessc",
                    file_path]

        elif file_type == '.sass':
            output_file = join(working_dir, file_name + '.css')
            cmd = ["/usr/local/bin/sass", file_path, output_file]

        elif file_type == '.scss':
            output_file = join(working_dir, file_name + '.css')
            cmd = ["/usr/local/bin/scss", file_path, output_file]

        else:
            return []
        # finally execute our command
        view.window().run_command("exec_redir", {"cmd": cmd, "quiet": True,
                         "redir": redir})
