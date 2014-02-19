# -*- coding: utf-8 -*-
"""
  user_config.py: a module to specify installation-specific settings for
                the wormpy module
  
  This file should be synced once, then included in your .gitignore file, 
  and then overridden with your custom settings (if necessary)
  
  @authors: @JimHokanson, @MichaelCurrie
  
"""


DROPBOX_PATH = "C:\\Users\\Michael\\Dropbox\\"

# An unc-8 (strong coiler) mutant worm
WORM_FILE_PATH = "worm_data\\example_feature_files\\" + \
                 "unc-8 (rev) on food " + \
                 "R_2010_03_19__09_14_57___2___2_features.mat"

NORMALIZED_WORM_PATH = "worm_data\\video\\testing_with_GUI\\.data\\" + \
                       "mec-4 (u253) off food " + \
                       "x_2010_04_21__17_19_20__1_seg\\normalized"



#  OLD CODE (for reference):
  

  # DEBUG: hardcoded for now.
#  worm_file_path = os.path.join(base_path, 
#                               r"worm_data\example_feature_files\\" +
#                               "unc-8 (rev) on food " +
#                               "R_2010_03_19__09_14_57___2___2_features.mat")


#  def get_user_data_path():
#  # 
#  #  Return the data path to be used to load example worm files.
#  #  This path will change depending on where DropBox has been located
  #  on the user computer.

#    if(getpass.getuser() == 'Michael'):
#      # michael's computer at home
#      user_data_path = r"C:\Users\Michael\Dropbox\\"
#    elif(getpass.getuser() == 'mcurrie'):
#      # michael's computer at work
#      user_data_path = r"C:\Backup\Dropbox\\"
#    else:
#      # if it's not Michael, assume it's Jim
#      if(os.name == 'nt'): 
#        # Jim is using Windows
#        user_data_path = "F:\\"
#      else:
#        # otherwise, Jim is probably using his Mac
#        user_data_path = r"/Users/jameshokanson/Dropbox"
#    
#    return user_data_path  