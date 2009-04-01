import subprocess
import remove_unversioned_files
import sys
import os


#=======================================================================================================================
# Execute
#=======================================================================================================================
def Execute(cmds, env=None):
    print 'Executing', ' '.join(cmds), ':', subprocess.call(cmds, env=env)


#=======================================================================================================================
# Make
#=======================================================================================================================
def Make():
    base_dir = r'W:\temp_buildDir'
    pydev_pro_dir = base_dir+r'\pydev_pro'
    pydev_dir = base_dir+r'\pydev'
    
    initial_dir = os.getcwd()
    try:
        os.chdir(pydev_pro_dir)
        
        for d in (pydev_dir, pydev_pro_dir):
        
            Execute(['svn', 'revert', '-R', d])
            remove_unversioned_files.RemoveFilesFrom(d)
            Execute(['svn', 'up', '--non-interactive', '--force', d])
    
            env = {}
            env.update(os.environ)
            
            env['PATH'] = env['PATH']+os.pathsep+r'W:\eclipse_341_clean\plugins\org.apache.ant_1.7.0.v200803061910\bin'
            env['JAVA_HOME'] = r'D:\bin\jdk_1_5_09'
            
            if d.endswith('pro'):
                os.chdir(pydev_pro_dir+r'\builders\com.python.pydev.build')
            else:
                os.chdir(pydev_pro_dir+r'\builders\org.python.pydev.build')
            
            cmds = [
                'ant',
                 '-DbuildDirectory=W:/temp_buildDir/pydev',
                 '-Dbaseos=win32',
                 '-Dbasews=win32',
                 '-Dbasearch=x86',
                 '-Ddeploy.dir=w:/temp_deployDir/pydev',
                 '-DcleanAfter=false',
                 '-Dvanilla.eclipse=W:/eclipse_341_clean'
            ]
            Execute(cmds, env)
    finally:
        os.chdir(initial_dir)

        


#=======================================================================================================================
# main
#=======================================================================================================================
if __name__ == '__main__':
    Make()