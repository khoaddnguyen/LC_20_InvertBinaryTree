def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    # swap the children
    tempt_position = root.left
    root.left = root.right
    root.right = tempt_position

    # recursively invert the subtree
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
